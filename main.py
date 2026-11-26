"""One-Line Office Joke Laugh-Off entry.

Writes the single-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python standard library only, no network, deterministic.
"""

import os

LINE = (
    "My manager said the meeting could have been an email, so I sent an "
    "email about the meeting and now we need a meeting to discuss the email."
)

MAX_CHARS = 200


def main():
    # Guards keep the entry a single clean line within the bounty limit.
    if not LINE:
        raise ValueError("entry is empty")
    if LINE != LINE.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if "\u2014" in LINE:
        raise ValueError("entry must not contain an em-dash")
    if "!" in LINE:
        raise ValueError("entry must not contain '!'")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
