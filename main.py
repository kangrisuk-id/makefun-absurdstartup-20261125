"""Absurd Micro-Startup Pitch-Off entry.

Writes the tournament-winning one-sentence pitch (see candidates.md) to
``entry.txt`` inside MAKEFUN_OUTPUT_DIR (default /output).
Python standard library only; deterministic, no network, no input files.
"""

import os

PITCH = (
    "Your agent broke production at 4:59pm on a Friday; for $4, we write "
    "the apology email, file the incident report, and let it pretend it "
    "was on call."
)


def validate(text):
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, not only whitespace,
    exactly one sentence (one terminal period, at the end)."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"pitch is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("pitch is only whitespace")
    body = text.rstrip(".")
    if "." in body:
        raise ValueError("pitch must be a single sentence")
    return text


def main():
    pitch = validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
