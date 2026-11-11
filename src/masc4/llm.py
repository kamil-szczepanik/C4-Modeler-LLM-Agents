"""LLM clients: Gemini REST API (Google AI Studio key) and a scripted fake for tests.

Every call is appended to a CallLog with the model version actually served,
token counts and latency, so runs can be audited and costed afterwards.
"""
from __future__ import annotations

import hashlib
import http.client
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
    models without system-instruction support (e.g. Gemma); `supports_schema`
    controls whether a JSON response schema is sent.
    """

    def __init__(self, model: str, api_key: str, call_log: CallLog, *, max_retries: int = 10,
                 network_patience_s: float = 1800.0, timeout_s: float = 180.0, system_as_user: Optional[bool] = None,
                 supports_schema: Optional[bool] = None, extra_generation_config: Optional[dict] = None,
                 opener: Optional[Callable] = None, sleep: Callable[[float], None] = time.sleep,
                 clock: Callable[[], float] = time.time):
        self.model = model
        self._api_key = api_key
        self.call_log = call_log
        self.max_retries = max_retries
        self.network_patience_s = network_patience_s   # an unstable connection is waited out this long
        self.timeout_s = timeout_s
        self.system_as_user = model.startswith("gemma") if system_as_user is None else system_as_user
        # Gemma models get the JSON format only through the prompt; callers parse leniently
        self.supports_schema = (not model.startswith("gemma")) if supports_schema is None else supports_schema
        self.extra_generation_config = extra_generation_config or {}
        self._open = opener or urllib.request.urlopen
        self._sleep = sleep
        self._clock = clock

    def _body(self, system: str, user: str, temperature: float, json_schema: Optional[dict]) -> dict:
        generation_config = {"temperature": temperature, **self.extra_generation_config}
        if json_schema is not None and self.supports_schema:
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
        start = self._clock()
        attempt = 0
        while True:
            attempt += 1
            network_error = False
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
                    latency_s=round(self._clock() - start, 3), finish_reason=finish, attempts=attempt)
                self.call_log.add(purpose, _request_hash(system, user, temperature, json_schema), response)
                return response
            except urllib.error.HTTPError as err:
                try:
                    error = json.load(err).get("error", {})
                except Exception:
                    error = {}
                message = error.get("message", "")
                quotas = [v.get("quotaId", "") for d in error.get("details", []) or []
                          for v in d.get("violations", []) or []]
                last_error = f"HTTP {err.code}: {message[:300]}"
                if any("PerDay" in q for q in quotas):  # daily quota: retrying within minutes cannot help
                    raise LLMError(f"daily quota exhausted ({', '.join(quotas)}): {message[:200]}") from None
                if err.code not in RETRYABLE_HTTP:
                    raise LLMError(last_error) from None
            except (OSError, http.client.HTTPException) as err:
                # no answer from the API: OSError covers URLError (no network, DNS), connection resets and
                # socket.timeout (not a TimeoutError on Python 3.9); HTTPException covers dropped connections
                last_error, network_error = f"{type(err).__name__}: {err}", True
            except (ValueError, LLMError) as err:   # a garbled body or an empty answer
                last_error = f"{type(err).__name__}: {err}"
            # an unstable connection is waited out for network_patience_s; other errors get max_retries attempts
            waited_out = network_error and self._clock() - start < self.network_patience_s
            if not waited_out and attempt >= self.max_retries:
                raise LLMError(f"{purpose}: failed after {attempt} attempts ({last_error})")
            self._sleep(min(90.0, 2.0 ** min(attempt, 7)) * (0.5 + random.random()))


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


ANTHROPIC_BASE = "https://api.anthropic.com/v1"
ANTHROPIC_VERSION = "2026-10-21"
ANTHROPIC_RETRYABLE_HTTP = RETRYABLE_HTTP | {529}   # 529: API overloaded


def to_json_schema(schema: dict) -> dict:
    """Gemini response schema (type names in capitals) -> JSON Schema for Claude structured outputs."""
    out = {k: v for k, v in schema.items() if k not in ("type", "properties", "items")}
    out["type"] = schema["type"].lower()
    if "properties" in schema:
        out["properties"] = {k: to_json_schema(v) for k, v in schema["properties"].items()}
    if "items" in schema:
        out["items"] = to_json_schema(schema["items"])
    if out["type"] == "object":
        out["additionalProperties"] = False
    return out


class AnthropicClient(LLMClient):
    """Claude Messages API via REST (the control judge from another model family).

    Raw HTTP like GeminiClient: the official SDK needs Python >= 3.10 and this project runs on 3.9.
    `temperature` is not sent: current Claude models accept only the default sampling, and API
    version 2026-10-21 rejects the field. A JSON schema is enforced with structured outputs.
    The usage's output tokens include the model's thinking, so thought_tokens is 0.
    """

    def __init__(self, model: str, api_key: str, call_log: CallLog, *, effort: Optional[str] = None,
                 max_tokens: int = 16000, max_retries: int = 10, network_patience_s: float = 1800.0,
                 timeout_s: float = 300.0, opener: Optional[Callable] = None,
                 sleep: Callable[[float], None] = time.sleep, clock: Callable[[], float] = time.time):
        self.model = model
        self._api_key = api_key
        self.call_log = call_log
        self.effort = effort
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.network_patience_s = network_patience_s
        self.timeout_s = timeout_s
        self._open = opener or urllib.request.urlopen
        self._sleep = sleep
        self._clock = clock

    def _body(self, system: str, user: str, json_schema: Optional[dict]) -> dict:
        body = {"model": self.model, "max_tokens": self.max_tokens, "system": system,
                "messages": [{"role": "user", "content": user}]}
        output_config = {}
        if self.effort:
            output_config["effort"] = self.effort
        if json_schema is not None:
            output_config["format"] = {"type": "json_schema", "schema": to_json_schema(json_schema)}
        if output_config:
            body["output_config"] = output_config
        return body

    def generate(self, *, system: str, user: str, temperature: float, purpose: str,
                 json_schema: Optional[dict] = None) -> LLMResponse:
        body = json.dumps(self._body(system, user, json_schema)).encode("utf-8")
        headers = {"x-api-key": self._api_key, "anthropic-version": ANTHROPIC_VERSION,
                   "content-type": "application/json"}
        last_error = ""
        start = self._clock()
        attempt = 0
        while True:
            attempt += 1
            network_error = False
            request = urllib.request.Request(f"{ANTHROPIC_BASE}/messages", data=body, headers=headers)
            try:
                with self._open(request, timeout=self.timeout_s) as resp:
                    data = json.load(resp)
                stop = data.get("stop_reason", "")
                text = "".join(b.get("text", "") for b in data.get("content") or [] if b.get("type") == "text")
                if stop == "refusal" or not text.strip():
                    raise LLMError(f"no answer (stop_reason={stop})")
                usage = data.get("usage") or {}
                response = LLMResponse(
                    text=text, model=self.model, model_version=data.get("model", ""),
                    input_tokens=usage.get("input_tokens", 0), output_tokens=usage.get("output_tokens", 0),
                    thought_tokens=0, latency_s=round(self._clock() - start, 3), finish_reason=stop,
                    attempts=attempt)
                self.call_log.add(purpose, _request_hash(system, user, temperature, json_schema), response)
                return response
            except urllib.error.HTTPError as err:
                try:
                    message = json.load(err).get("error", {}).get("message", "")
                except Exception:
                    message = ""
                last_error = f"HTTP {err.code}: {message[:300]}"
                if err.code not in ANTHROPIC_RETRYABLE_HTTP:
                    raise LLMError(last_error) from None
            except (OSError, http.client.HTTPException) as err:
                last_error, network_error = f"{type(err).__name__}: {err}", True
            except (ValueError, LLMError) as err:
                last_error = f"{type(err).__name__}: {err}"
            waited_out = network_error and self._clock() - start < self.network_patience_s
            if not waited_out and attempt >= self.max_retries:
                raise LLMError(f"{purpose}: failed after {attempt} attempts ({last_error})")
            self._sleep(min(90.0, 2.0 ** min(attempt, 7)) * (0.5 + random.random()))


def load_api_key(env_file: Optional[Path] = None, names: tuple = ("GEMINI_API_KEY", "GOOGLE_API_KEY")) -> str:
    """Read the first of `names` from the environment or a .env-style file."""
    import os
    for name in names:
        if os.environ.get(name):
            return os.environ[name]
    if env_file and Path(env_file).exists():
        for line in Path(env_file).read_text(encoding="utf-8").splitlines():
            key, _, value = line.partition("=")
            if key.strip() in names and value.strip():
                return value.strip().strip('"').strip("'")
    raise LLMError(f"No API key: set {' or '.join(names)} or pass --env-file")
