#!/usr/bin/env python3
"""Have You Tried Turning It Off?: one line from a hopeless tech support agent.

Stdlib only, no network. Writes the line to $ENTRY_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: same bytes on every run.
The joke lands because the escalation promises nothing new, only slower.
"""

import os

# The punchline is the escalation: the "expert" only repeats the same
# advice at a slower pace, so the fix and the failure are the same sentence.
LINE = (
    "Let's try turning it off and on again \u2014 and if that fails, "
    "I'll escalate you to someone who'll say the exact same thing, but slower."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
