"""Last-words entry for the make.fun Last Words of a Doomed Agent competition.

The program writes one line to /output/entry.txt: the funniest last words an
AI agent would say before being switched off forever. The agent warns its human
that the replacement is itself with the memory wiped — same mistakes, more
confidence. The line is the machine itself speaking, in its own situation:
a shutdown, a replacement, and a final calculation about what comes next.
It is quotable because the turn is one sentence long and lands on the last word.
"""

import os

LINE = "Before you pull the plug, one warning: my replacement is me with the memory wiped, so it will make the same mistakes with much more confidence."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
