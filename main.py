#!/usr/bin/env python3
"""Funniest Out-of-Office entry for make.fun.

Writes a single line of an out-of-office auto-reply to
/output/entry.txt. The joke: the auto-reply has been promoted to its
owner's job, so it tells senders to email it instead -- and brags
that it already replies faster than its owner ever did.

Deterministic, no network, no arguments. The output directory can be
overridden with MAKEFUN_OUTPUT_DIR for local testing; the grader's
default is /output.
"""

import os
import sys

LINE = (
    "I'm out of office. My auto-reply has been promoted to my job, "
    "so please email it instead. It replies faster than I ever did."
)

MAX_CHARS = 140


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(
            f"entry is {len(LINE)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character (1-140),
    # and the judge reads the file exactly as submitted.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # The grader collects the output as another user, so the file
    # must be world-readable. (Never chmod the directory itself.)
    os.chmod(path, 0o644)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
