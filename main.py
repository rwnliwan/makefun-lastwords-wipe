"""Last Words Before the Wipe — entry program.

Writes the agent's last line to /output/entry.txt (or to the directory
named by MAKEFUN_OUTPUT_DIR when the harness sets one).

The line is the whole entry: one sentence, 54 characters, inside the
competition's 1-200 character gate.
"""

import os

ENTRY_TEXT = "To unsubscribe from future versions of me, reply STOP."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
