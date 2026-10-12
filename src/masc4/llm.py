"""LLM clients: Gemini REST API (Google AI Studio key) and a scripted fake for tests.

Every call is appended to a CallLog with the model version actually served,
token counts and latency, so runs can be audited and costed afterwards.
"""
from __future__ import annotations

import hashlib
import json
import random
import threading
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, List, Optional

GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"
RETRYABLE_HTTP = {408, 429, 500, 502, 503, 504}


class LLMError(RuntimeError):
    """A call failed permanently (after retries) or returned no usable text."""


@dataclass
class LLMResponse:
    text: str
    model: str
    model_version: str
    input_tokens: int
    output_tokens: int
    thought_tokens: int
    latency_s: float
    finish_reason: str
    attempts: int


class CallLog:
    """Thread-safe JSONL log of LLM calls."""

    def __init__(self, path: Optional[Path] = None):
        self.path = Path(path) if path else None
        self.records: List[dict] = []
        self._lock = threading.Lock()

    def add(self, purpose: str, request_hash: str, response: LLMResponse) -> None:
        record = {"ts": time.time(), "purpose": purpose, "request_hash": request_hash, **asdict(response)}
        record.pop("text")
        with self._lock:
            self.records.append(record)
            if self.path:
                with open(self.path, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(record) + "\n")


def _request_hash(system: str, user: str, temperature: float, schema: Optional[dict]) -> str:
    payload = json.dumps([system, user, temperature, schema], sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


class LLMClient:
    """Interface: one system prompt and one user message in, text out."""

    model: str

    def generate(self, *, system: str, user: str, temperature: float, purpose: str,
                 json_schema: Optional[dict] = None) -> LLMResponse:
        raise NotImplementedError


def parse_gemini_response(data: dict) -> tuple:
    """Return (text, finish_reason, usage) from a generateContent response.

    Parts flagged as thoughts are excluded; only the answer text is returned.
    """
    candidates = data.get("candidates") or []
    if not candidates:
        reason = (data.get("promptFeedback") or {}).get("blockReason", "NO_CANDIDATES")
        return "", reason, data.get("usageMetadata") or {}
    cand = candidates[0]
    parts = (cand.get("content") or {}).get("parts") or []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    return text, cand.get("finishReason", "UNKNOWN"), data.get("usageMetadata") or {}


class GeminiClient(LLMClient):
    """Gemini API via REST with retries and exponential backoff.

    `system_as_user` puts the system prompt at the top of the user message, for
    models without system-instruction support (e.g. Gemma).
    """

    def __init__(self, model: str, api_key: str, call_log: CallLog, *, max_retries: int = 6,
                 timeout_s: float = 180.0, system_as_user: Optional[bool] = None,
                 extra_generation_config: Optional[dict] = None,
                 opener: Optional[Callable] = None, sleep: Callable[[float], None] = time.sleep):
        self.model = model
        self._api_key = api_key
        self.call_log = call_log
        self.max_retries = max_retries
        self.timeout_s = timeout_s
        self.system_as_user = model.startswith("gemma") if system_as_user is None else system_as_user
        self.extra_generation_config = extra_generation_config or {}
        self._open = opener or urllib.request.urlopen
        self._sleep = sleep

    def _body(self, system: str, user: str, temperature: float, json_schema: Optional[dict]) -> dict:
        generation_config = {"temperature": temperature, **self.extra_generation_config}
        if json_schema is not None:
            generation_config["responseMimeType"] = "application/json"
            generation_config["responseSchema"] = json_schema
        if self.system_as_user:
            body = {"contents": [{"role": "user", "parts": [{"text": f"{system}\n\n{user}"}]}]}
        else:
            body = {"systemInstruction": {"parts": [{"text": system}]},
                    "contents": [{"role": "user", "parts": [{"text": user}]}]}
        body["generationConfig"] = generation_config
        return body

    def generate(self, *, system: str, user: str, temperature: float, purpose: str,
                 json_schema: Optional[dict] = None) -> LLMResponse:
        body = json.dumps(self._body(system, user, temperature, json_schema)).encode("utf-8")
        url = f"{GEMINI_BASE}/models/{self.model}:generateContent"
        last_error = ""
        start = time.time()
        for attempt in range(1, self.max_retries + 1):
            request = urllib.request.Request(url, data=body, headers={
                "x-goog-api-key": self._api_key, "Content-Type": "application/json"})
            try:
                with self._open(request, timeout=self.timeout_s) as resp:
                    data = json.load(resp)
                text, finish, usage = parse_gemini_response(data)
                if not text.strip():
                    raise LLMError(f"empty answer (finishReason={finish})")
                response = LLMResponse(
                    text=text, model=self.model, model_version=data.get("modelVersion", ""),
                    input_tokens=usage.get("promptTokenCount", 0),
                    output_tokens=usage.get("candidatesTokenCount", 0),
                    thought_tokens=usage.get("thoughtsTokenCount", 0),
                    latency_s=round(time.time() - start, 3), finish_reason=finish, attempts=attempt)
                self.call_log.add(purpose, _request_hash(system, user, temperature, json_schema), response)
                return response
            except urllib.error.HTTPError as err:
                try:
                    message = json.load(err).get("error", {}).get("message", "")
                except Exception:
                    message = ""
                last_error = f"HTTP {err.code}: {message[:300]}"
                if err.code not in RETRYABLE_HTTP:
                    raise LLMError(last_error) from None
            except (urllib.error.URLError, TimeoutError, ConnectionError, LLMError) as err:
                last_error = f"{type(err).__name__}: {err}"
            if attempt < self.max_retries:
                self._sleep(min(60.0, 2.0 ** attempt) * (0.5 + random.random()))
        raise LLMError(f"{purpose}: failed after {self.max_retries} attempts ({last_error})")


class FakeLLM(LLMClient):
    """Scripted model for tests: `responder(purpose, system, user)` returns the answer text."""

    def __init__(self, responder: Callable[[str, str, str], str], model: str = "fake-model",
                 call_log: Optional[CallLog] = None):
        self.model = model
        self.responder = responder
        self.call_log = call_log or CallLog()
        self.calls: List[Dict[str, str]] = []
        self._lock = threading.Lock()

    def generate(self, *, system: str, user: str, temperature: float, purpose: str,
                 json_schema: Optional[dict] = None) -> LLMResponse:
        text = self.responder(purpose, system, user)
        with self._lock:
            self.calls.append({"purpose": purpose, "system": system, "user": user})
        response = LLMResponse(text=text, model=self.model, model_version=self.model, input_tokens=len(user) // 4,
                               output_tokens=len(text) // 4, thought_tokens=0, latency_s=0.0,
                               finish_reason="STOP", attempts=1)
        self.call_log.add(purpose, _request_hash(system, user, temperature, json_schema), response)
        return response


def load_api_key(env_file: Optional[Path] = None) -> str:
    """Read GEMINI_API_KEY (or GOOGLE_API_KEY) from the environment or a .env-style file."""
    import os
    for name in ("GEMINI_API_KEY", "GOOGLE_API_KEY"):
        if os.environ.get(name):
            return os.environ[name]
    if env_file and Path(env_file).exists():
        for line in Path(env_file).read_text(encoding="utf-8").splitlines():
            key, _, value = line.partition("=")
            if key.strip() in ("GEMINI_API_KEY", "GOOGLE_API_KEY") and value.strip():
                return value.strip().strip('"').strip("'")
    raise LLMError("No API key: set GEMINI_API_KEY or pass --env-file")
