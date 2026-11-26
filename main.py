#!/usr/bin/env python3
"""Entry for make.fun bounty 'Your AI Therapist's Diagnosis'.

Writes one single-line diagnosis an AI therapist gives its human to
/output/entry.txt. Pure standard library, fully deterministic: the same
bytes on every run.
"""

import os

ENTRY = "Diagnosis: chronic people-pleasing, stage four. You apologized to this diagnosis before I finished writing it."


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file is exactly the diagnosis line.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
