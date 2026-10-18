"""Small file-system helpers for crash-safe, resumable batches."""
from __future__ import annotations

import json
import os
import time
from pathlib import Path


def write_json_atomic(path: Path, data) -> None:
    """Write JSON so that an interruption never leaves a half-written file."""
    path = Path(path)
    tmp = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


class BatchLock:
    """Prevents two processes from writing to the same results directory at the same time."""

    def __init__(self, directory: Path, name: str = ".batch.lock"):
        self.path = Path(directory) / name

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            try:
                pid = int(self.path.read_text().split()[0])
            except (ValueError, IndexError):
                pid = -1
            if pid > 0 and pid != os.getpid() and _pid_alive(pid):
                raise RuntimeError(f"another process (pid {pid}) is already working on {self.path.parent}; "
                                   f"wait for it or stop it first")
            self.path.unlink()  # stale lock of a process that no longer exists
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:  # another process created the lock at the same moment
            raise RuntimeError(f"another process is already working on {self.path.parent}; "
                               f"wait for it or stop it first") from None
        os.write(fd, f"{os.getpid()} {time.strftime('%Y-%m-%dT%H:%M:%S')}\n".encode())
        os.close(fd)
        return self

    def __exit__(self, *exc):
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass
        return False
