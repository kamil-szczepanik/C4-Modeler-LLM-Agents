"""API prices (USD per 1M tokens: input, output) from ai.google.dev/gemini-api/docs/pricing (Oct 2026).

Thinking tokens are billed as output tokens. Models missing here (e.g. Gemma) are free of charge.
Used for cost estimates in the progress monitor and for the --max-cost safety stop.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

PRICES = {
    "gemini-3.5-flash-lite": (0.30, 2.50),
    "gemini-3.1-flash-lite": (0.25, 1.50),
    "gemini-3.8-flash": (0.75, 3.75),
    "gemini-3.6-flash": (0.75, 3.75),
}


def cost_of(records: Iterable[dict]) -> float:
    total = 0.0
    for r in records:
        price_in, price_out = PRICES.get(r.get("model", ""), (0.0, 0.0))
        total += (r.get("input_tokens", 0) * price_in
                  + (r.get("output_tokens", 0) + r.get("thought_tokens", 0)) * price_out) / 1e6
    return total


def cost_of_log(path: Path) -> float:
    if not Path(path).exists():
        return 0.0
    records = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return cost_of(records)
