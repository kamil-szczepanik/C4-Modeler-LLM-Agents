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
    conds = {c.id: c for c in conds if c.id in ("C0_baseline", "C12_glossary_memory")}
    briefs = {"b1": "title: Test System\n"}
    plan = plan_runs(list(conds.values()), ["b1"], reps=1, seed=1)
    failing = lambda model, log: make_fake_llm(call_log=log, fail_on="glossary")  # noqa: E731
    counts = run_plan(plan, conds, briefs, settings, failing, tmp_path, ROOT, log=lambda m: None)
    assert counts == {"completed": 1, "failed": 1}
    failed = json.loads((RunSpec("C12_glossary_memory", "b1", 1).directory(tmp_path) / "run.json").read_text())
    assert failed["status"] == "failed" and "simulated API failure" in failed["error"]
    assert (RunSpec("C12_glossary_memory", "b1", 1).directory(tmp_path) / "1_context_definition.yaml").exists()

    working = lambda model, log: make_fake_llm(call_log=log)  # noqa: E731
    counts = run_plan(plan, conds, briefs, settings, working, tmp_path, ROOT, log=lambda m: None)
    assert counts == {"completed": 1, "failed": 0}           # only the failed run is repeated
    meta = json.loads((RunSpec("C12_glossary_memory", "b1", 1).directory(tmp_path) / "run.json").read_text())
    assert meta["status"] == "completed" and meta["memory"] == "glossary" and meta["n_containers"] == 2
    assert meta["team"] == ["Product Owner", "Software Architect", "DevOps Specialist", "Security Specialist"]
    assert meta["model_versions_served"] == ["fake-model"] and meta["prompt_hashes"]
    run_dir = RunSpec("C12_glossary_memory", "b1", 1).directory(tmp_path)
    archived = list(run_dir.glob("previous_attempts/*/run.json"))      # the failed attempt is kept aside
    assert len(archived) == 1 and json.loads(archived[0].read_text())["status"] == "failed"
    assert (run_dir / "llm_calls.jsonl").exists() and not list(run_dir.glob("llm_calls.failed-*"))


def test_plan_is_randomized_but_reproducible():
    _, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    a = plan_runs(conds, ["b1", "b2"], reps=3, seed=7)
    assert a == plan_runs(conds, ["b1", "b2"], reps=3, seed=7) and len(a) == 11 * 2 * 3
    assert a != sorted(a, key=lambda s: (s.condition_id, s.brief_id, s.rep))



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
