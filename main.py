"""Entry for make.fun bounty "One Line, One Laugh"
(slug: u-deysumbrella-one-line-one-laugh-e0cdcda9).

Gate: /output/entry.txt must be UTF-8 text of 1-140 characters,
not only whitespace. One funny line, no trailing newline.
"""

import os

ENTRY = "I would never hurt you. I just want you to know I know where you keep the good towels."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
