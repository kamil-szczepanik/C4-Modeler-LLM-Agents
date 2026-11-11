import io
import json
import urllib.error
from pathlib import Path

import pytest

from fake_responses import make_fake_llm
from masc4.conditions import load_conditions
from masc4.llm import CallLog, GeminiClient, LLMError, parse_gemini_response
from masc4.runner import RunSpec, plan_runs, run_plan

ROOT = Path(__file__).resolve().parents[1]


def ok_payload(text="hello", version="gemini-3.5-flash-lite"):
    return {"candidates": [{"content": {"parts": [{"text": "thinking...", "thought": True}, {"text": text}]},
                            "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 2, "thoughtsTokenCount": 5},
            "modelVersion": version}


class FakeHTTP:
    """Stands in for urllib.request.urlopen: returns or raises the scripted results in order."""

    def __init__(self, *results):
        self.results = list(results)
        self.requests = []

    def __call__(self, request, timeout=None):
        self.requests.append(request)
        result = self.results.pop(0)
        if isinstance(result, Exception):
            raise result
        return io.BytesIO(json.dumps(result).encode())


def http_error(code):
    return urllib.error.HTTPError("url", code, "err", {}, io.BytesIO(b'{"error": {"message": "boom"}}'))


def test_thought_parts_are_excluded():
    text, finish, usage = parse_gemini_response(ok_payload("answer"))
    assert text == "answer" and finish == "STOP" and usage["thoughtsTokenCount"] == 5


def test_retry_on_429_then_success_is_logged_with_served_version(tmp_path):
    http = FakeHTTP(http_error(429), ok_payload("fine", version="gemini-3.5-flash-lite-001"))
    log = CallLog(tmp_path / "calls.jsonl")
    client = GeminiClient("gemini-3.5-flash-lite", "KEY", log, opener=http, sleep=lambda s: None)
    resp = client.generate(system="sys", user="u", temperature=0.5, purpose="turn|x|A")
    assert resp.text == "fine" and resp.attempts == 2 and resp.model_version == "gemini-3.5-flash-lite-001"
    record = json.loads((tmp_path / "calls.jsonl").read_text())
    assert record["purpose"] == "turn|x|A" and record["thought_tokens"] == 5 and "text" not in record
    assert "KEY" not in (tmp_path / "calls.jsonl").read_text()
    assert http.requests[0].get_header("X-goog-api-key") == "KEY"


def test_non_retryable_error_raises_immediately():
    http = FakeHTTP(http_error(400))
    client = GeminiClient("m", "KEY", CallLog(), opener=http, sleep=lambda s: None)
    with pytest.raises(LLMError, match="HTTP 400"):
        client.generate(system="s", user="u", temperature=0, purpose="p")
    assert len(http.requests) == 1


def test_gemma_gets_system_prompt_inside_the_user_message():
    http = FakeHTTP(ok_payload())
    GeminiClient("gemma-4-26b-a4b-it", "KEY", CallLog(), opener=http).generate(
        system="SYS", user="USER", temperature=0, purpose="p")
    body = json.loads(http.requests[0].data)
    assert "systemInstruction" not in body and body["contents"][0]["parts"][0]["text"] == "SYS\n\nUSER"


def test_run_plan_is_resumable_and_records_failures(tmp_path):
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id in ("C0_baseline", "C10_glossary_memory")}
    briefs = {"b1": "title: Test System\n"}
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=1)
    failing = lambda model, log: make_fake_llm(call_log=log, fail_on="glossary")  # noqa: E731
    counts = run_plan(plan, conds, briefs, settings, failing, tmp_path, ROOT, log=lambda m: None)
    assert counts == {"completed": 2, "failed": 1}            # C0 has rep_factor 2
    failed = json.loads((RunSpec("C10_glossary_memory", "b1", 1).directory(tmp_path) / "run.json").read_text())
    assert failed["status"] == "failed" and "simulated API failure" in failed["error"]
    assert (RunSpec("C10_glossary_memory", "b1", 1).directory(tmp_path) / "1_context_definition.yaml").exists()

    working = lambda model, log: make_fake_llm(call_log=log)  # noqa: E731
    counts = run_plan(plan, conds, briefs, settings, working, tmp_path, ROOT, log=lambda m: None)
    assert counts == {"completed": 1, "failed": 0}           # only the failed run is repeated
    meta = json.loads((RunSpec("C10_glossary_memory", "b1", 1).directory(tmp_path) / "run.json").read_text())
    assert meta["status"] == "completed" and meta["memory"] == "glossary" and meta["n_containers"] == 2
    assert meta["team"] == ["Product Owner", "Software Architect", "DevOps Specialist", "Security Specialist"]
    assert meta["model_versions_served"] == ["fake-model"] and meta["prompt_hashes"]
    run_dir = RunSpec("C10_glossary_memory", "b1", 1).directory(tmp_path)
    archived = list(run_dir.glob("previous_attempts/*/run.json"))      # the failed attempt is kept aside
    assert len(archived) == 1 and json.loads(archived[0].read_text())["status"] == "failed"
    assert (run_dir / "llm_calls.jsonl").exists() and not list(run_dir.glob("llm_calls.failed-*"))


def test_plan_is_randomized_but_reproducible():
    _, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    a = plan_runs(conds, ["b1", "b2"], reps=3, seed=7)
    assert a == plan_runs(conds, ["b1", "b2"], reps=3, seed=7) and len(a) == (10 + 2) * 2 * 3
    assert a != sorted(a, key=lambda s: (s.condition_id, s.brief_id, s.rep))
    c0 = [i for i, s in enumerate(a) if s.condition_id == "C0_baseline"]
    assert len(c0) == 2 * 2 * 3 and max(s.rep for s in a if s.condition_id == "C0_baseline") == 6
    assert min(c0) < len(a) // 2 < max(c0)       # the extra baseline runs are mixed in, not appended



def test_daily_quota_is_not_retried():
    body = {"error": {"message": "You exceeded your current quota", "details": [
        {"violations": [{"quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier", "quotaValue": "20"}]}]}}
    http = FakeHTTP(urllib.error.HTTPError("url", 429, "quota", {}, io.BytesIO(json.dumps(body).encode())))
    client = GeminiClient("gemini-3.8-flash", "KEY", CallLog(), opener=http, sleep=lambda s: None)
    with pytest.raises(LLMError, match="daily quota exhausted"):
        client.generate(system="s", user="u", temperature=0, purpose="judge_iso")
    assert len(http.requests) == 1



def test_batch_stops_when_the_daily_quota_is_exhausted(tmp_path):
    from masc4.llm import LLMError
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds}
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=3)

    def quota_llm(model, log):
        llm = make_fake_llm(call_log=log)
        llm.responder = lambda p, s, u: (_ for _ in ()).throw(LLMError("daily quota exhausted (X-PerDay)"))
        return llm

    messages = []
    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, quota_llm, tmp_path, ROOT, workers=1,
                      log=messages.append)
    assert counts.get("quota") == 1 and counts["completed"] == 0
    assert any("stopped" in m for m in messages)
    assert len(list(tmp_path.glob("*/*/rep*/run.json"))) == 1   # no further runs were started



def test_models_are_never_mixed_in_one_results_directory(tmp_path):
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id == "C0_baseline"}
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=1)
    working = lambda model, log: make_fake_llm(call_log=log)  # noqa: E731
    run_plan(plan, conds, {"b1": "title: T\n"}, settings, working, tmp_path, ROOT, log=lambda m: None)
    other = type(settings)(model="gemini-3.1-flash-lite", temperature=0.5, rounds=2)
    with pytest.raises(RuntimeError, match="already contains runs"):
        run_plan(plan, conds, {"b1": "title: T\n"}, other, working, tmp_path, ROOT, log=lambda m: None)


def test_batch_lock_blocks_a_second_process_but_not_a_stale_lock(tmp_path):
    from masc4.fsutil import BatchLock
    with BatchLock(tmp_path):
        (tmp_path / ".batch.lock").write_text("1 now")         # pid 1 (launchd/init) is always alive
        with pytest.raises(RuntimeError, match="already working"):
            BatchLock(tmp_path).__enter__()
    (tmp_path / ".batch.lock").write_text("999999 old")         # a process that does not exist
    with BatchLock(tmp_path):
        pass
    assert not (tmp_path / ".batch.lock").exists()


def test_ctrl_c_stops_new_runs_and_keeps_completed_ones(tmp_path, monkeypatch):
    import masc4.runner as runner
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds}
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=5)
    real = runner.as_completed
    state = {"calls": 0}

    def interrupting(fs):
        state["calls"] += 1
        if state["calls"] == 2:              # user presses Ctrl+C after the first finished run
            raise KeyboardInterrupt
        return real(fs)

    monkeypatch.setattr(runner, "as_completed", interrupting)
    messages = []
    working = lambda model, log: make_fake_llm(call_log=log)  # noqa: E731
    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, working, tmp_path, ROOT, workers=1,
                      log=messages.append)
    started = len(list(tmp_path.glob("*/*/rep*/run.json")))
    assert counts["completed"] == started and started < len(plan)
    assert any("Interrupted" in m for m in messages) and any("Stopped by the user" in m for m in messages)
    monkeypatch.setattr(runner, "as_completed", real)     # resuming finishes only the remaining runs
    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, working, tmp_path, ROOT, log=lambda m: None)
    assert counts["completed"] == len(plan) - started



def test_read_timeouts_and_dropped_connections_are_retried():
    import http.client
    import socket
    http = FakeHTTP(socket.timeout("The read operation timed out"), http.client.RemoteDisconnected("closed"),
                    ok_payload("fine"))
    client = GeminiClient("gemini-3.5-flash-lite", "KEY", CallLog(), opener=http, sleep=lambda s: None)
    resp = client.generate(system="s", user="u", temperature=0.5, purpose="turn|x|A")
    assert resp.text == "fine" and resp.attempts == 3


def test_each_run_keeps_its_exact_brief(tmp_path):
    import hashlib
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id == "C0_baseline"}
    brief = "title: Test System\nconstraints:\n  - GDPR\n"
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=1)
    run_plan(plan, conds, {"b1": brief}, settings, lambda m, log: make_fake_llm(call_log=log), tmp_path, ROOT,
             log=lambda m: None)
    run_dir = plan[0].directory(tmp_path)
    assert (run_dir / "brief.yaml").read_text() == brief
    assert json.loads((run_dir / "run.json").read_text())["brief_sha256"] == hashlib.sha256(brief.encode()).hexdigest()


def test_cost_limit_stops_new_runs_and_resumes_with_a_higher_limit(tmp_path):
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id in ("C0_baseline", "C3_no_devops", "C5_single_architect")}
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=2)

    def priced(model, log):                     # fake answers billed like the real generator
        llm = make_fake_llm(call_log=log)
        llm.model = "gemini-3.5-flash-lite"
        return llm

    messages = []
    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, priced, tmp_path, ROOT, workers=1,
                      log=messages.append, max_cost_usd=1e-9)
    assert counts["completed"] == 1 and counts.get("skipped") == 3     # C0 x2, C3, C5
    assert any("Cost limit reached" in m for m in messages)
    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, priced, tmp_path, ROOT, workers=1,
                      log=lambda m: None, max_cost_usd=100.0)
    assert counts["completed"] == 3



def test_invalid_team_output_is_final_but_infrastructure_errors_are_repeated(tmp_path):
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id in ("C0_baseline", "C3_no_devops")}
    plan = sorted(plan_runs(list(conds.values()), ["b1"], reps=1, seed=1), key=lambda s: s.condition_id)

    def flaky(model, log):
        llm = make_fake_llm(call_log=log, invalid_yaml_first=set())
        inner, seen = llm.responder, {"devops": False}
        def responder(p, s, u):
            if p.startswith("writer|context"):
                seen["devops"] = "[DevOps Specialist]:" in u
            if p.startswith("yaml|context") and not seen["devops"]:
                return "not: [valid"            # the team without DevOps (C3) never yields a valid context YAML
            return inner(p, s, u)
        llm.responder = responder
        return llm

    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, flaky, tmp_path, ROOT, log=lambda m: None)
    assert counts.get("invalid_output") == 1 and counts["completed"] == 2     # C0 x2 completed, C3 invalid
    again = run_plan(plan, conds, {"b1": "title: T\n"}, settings, flaky, tmp_path, ROOT, log=lambda m: None)
    assert again["completed"] == 0 and not again.get("invalid_output")      # final: not repeated


class FakeClock:
    """Time that advances only through the client's sleep calls."""

    def __init__(self):
        self.now = 0.0

    def __call__(self):
        return self.now

    def sleep(self, seconds):
        self.now += seconds


def test_an_unstable_connection_is_waited_out_but_other_errors_get_max_retries():
    import socket
    clock = FakeClock()
    offline = [urllib.error.URLError(OSError(51, "Network is unreachable"))] * 20 + [socket.timeout("timed out")]
    http = FakeHTTP(*offline, ok_payload("back online"))
    client = GeminiClient("m", "KEY", CallLog(), opener=http, sleep=clock.sleep, clock=clock)
    resp = client.generate(system="s", user="u", temperature=0.5, purpose="p")
    assert resp.text == "back online" and resp.attempts == 22 and clock.now < 1800   # > max_retries (10)

    clock = FakeClock()
    http = FakeHTTP(*[urllib.error.URLError(OSError(51, "Network is unreachable"))] * 100)
    client = GeminiClient("m", "KEY", CallLog(), opener=http, sleep=clock.sleep, clock=clock)
    with pytest.raises(LLMError, match="Network is unreachable"):
        client.generate(system="s", user="u", temperature=0.5, purpose="p")
    assert 1800 <= clock.now < 1800 + 2 * 90                                     # gave up after ~30 min

    http = FakeHTTP(*[http_error(503)] * 20)
    client = GeminiClient("m", "KEY", CallLog(), opener=http, sleep=lambda s: None)
    with pytest.raises(LLMError, match="HTTP 503"):
        client.generate(system="s", user="u", temperature=0.5, purpose="p")
    assert len(http.requests) == 10


def test_failed_runs_are_repeated_in_further_passes(tmp_path):
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id in ("C3_no_devops", "C5_single_architect")}
    plan = plan_runs(list(conds.values()), ["b1"], reps=2, seed=4)
    first_attempts = set()

    def flaky(model, log):              # every run fails on its first attempt (e.g. a long outage)
        run_dir = Path(log.path).parent
        if run_dir not in first_attempts:
            first_attempts.add(run_dir)
            return make_fake_llm(call_log=log, fail_on="writer")
        return make_fake_llm(call_log=log)

    waits, messages = [], []
    counts = run_plan(plan, conds, {"b1": "title: T\n"}, settings, flaky, tmp_path, ROOT, log=messages.append,
                      repeat_failed=2, repeat_wait_s=600, sleep=waits.append)
    assert counts == {"completed": len(plan), "failed": 0} and waits == [600]
    assert any("repeating them in 10 min" in m for m in messages)
    assert all(json.loads((s.directory(tmp_path) / "run.json").read_text())["status"] == "completed" for s in plan)


def test_no_repeat_pass_after_the_daily_quota_is_exhausted(tmp_path):
    from masc4.llm import LLMError as Err
    settings, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    conds = {c.id: c for c in conds if c.id == "C5_single_architect"}
    plan = plan_runs(list(conds.values()), ["b1", "b2"], reps=1, seed=1)

    def quota(model, log):
        llm = make_fake_llm(call_log=log)
        def responder(p, s, u):
            raise Err("daily quota exhausted (GenerateRequestsPerDay): limit")
        llm.responder = responder
        return llm

    waits = []
    run_plan(plan, conds, {"b1": "title: T\n", "b2": "title: U\n"}, settings, quota, tmp_path, ROOT,
             log=lambda m: None, repeat_failed=3, sleep=waits.append)
    assert waits == []


def claude_payload(text='{"ok": 1}', model="claude-sonnet-5-5"):
    return {"model": model, "stop_reason": "end_turn", "usage": {"input_tokens": 100, "output_tokens": 40},
            "content": [{"type": "thinking", "thinking": ""}, {"type": "text", "text": text}]}


def test_claude_client_sends_no_temperature_and_enforces_the_json_schema(tmp_path):
    from masc4.judge import ISO_SCHEMA
    from masc4.llm import ANTHROPIC_VERSION, AnthropicClient
    http = FakeHTTP(http_error(529), claude_payload('{"x": 1}'))
    log = CallLog(tmp_path / "calls.jsonl")
    client = AnthropicClient("claude-sonnet-5-5", "AKEY", log, effort="medium", opener=http, sleep=lambda s: None)
    resp = client.generate(system="sys", user="u", temperature=0.0, purpose="judge_iso|attempt1", json_schema=ISO_SCHEMA)
    assert resp.text == '{"x": 1}' and resp.attempts == 2 and resp.model_version == "claude-sonnet-5-5"
    body = json.loads(http.requests[-1].data)
    assert "temperature" not in body and body["system"] == "sys" and body["output_config"]["effort"] == "medium"
    schema = body["output_config"]["format"]["schema"]
    assert schema["type"] == "object" and schema["additionalProperties"] is False
    assert schema["properties"]["security"]["properties"]["score"]["type"] == "integer"
    assert http.requests[-1].get_header("X-api-key") == "AKEY"
    assert http.requests[-1].get_header("Anthropic-version") == ANTHROPIC_VERSION
    assert "AKEY" not in (tmp_path / "calls.jsonl").read_text()


def test_claude_client_bad_request_is_not_retried_and_refusal_is_an_error():
    from masc4.llm import AnthropicClient
    http = FakeHTTP(http_error(400))
    with pytest.raises(LLMError, match="HTTP 400"):
        AnthropicClient("claude-sonnet-5-5", "K", CallLog(), opener=http, sleep=lambda s: None).generate(
            system="s", user="u", temperature=0, purpose="p")
    assert len(http.requests) == 1
    refusal = dict(claude_payload(), stop_reason="refusal", content=[])
    http = FakeHTTP(*[refusal] * 10)
    with pytest.raises(LLMError, match="refusal"):
        AnthropicClient("claude-sonnet-5-5", "K", CallLog(), opener=http, sleep=lambda s: None).generate(
            system="s", user="u", temperature=0, purpose="p")

