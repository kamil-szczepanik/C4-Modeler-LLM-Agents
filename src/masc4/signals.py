"""Uniform stop handling: Ctrl+C (SIGINT) and `kill` (SIGTERM) both request a graceful stop."""
from __future__ import annotations

import signal


def _request_stop(signum, frame):
    raise KeyboardInterrupt


def install_stop_handlers() -> None:
    signal.signal(signal.SIGINT, signal.default_int_handler)   # also when started from a non-interactive shell
    signal.signal(signal.SIGTERM, _request_stop)
