"""One sentence explaining the modern internet to a traveler from 1800.

Writes the entry to /output/entry.txt. Stdlib only, no network,
deterministic: the same sentence every run.
"""

import os

LINE = (
    "It is a post office with no horses and no ships, where a farmer in "
    "Ohio asks a sailor in Canton, seven thousand miles away, the price "
    "of tea, and the answer is back before his kettle boils."
)


def main() -> None:
    text = LINE + "\n"
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, per the bounty rules.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
