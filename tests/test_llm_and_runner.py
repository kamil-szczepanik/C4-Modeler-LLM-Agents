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
    assert list((RunSpec("C12_glossary_memory", "b1", 1).directory(tmp_path)).glob("llm_calls.failed-*.jsonl"))


def test_plan_is_randomized_but_reproducible():
    _, conds = load_conditions(ROOT / "configs/conditions_v2.yaml")
    a = plan_runs(conds, ["b1", "b2"], reps=3, seed=7)
    assert a == plan_runs(conds, ["b1", "b2"], reps=3, seed=7) and len(a) == 14 * 2 * 3
    assert a != sorted(a, key=lambda s: (s.condition_id, s.brief_id, s.rep))
