"""Pickup Lines for Machines — one line, one agent to another.

The entry is a single pickup line written as one AI agent flirting with
another AI agent. It leans on the model's own nature: training in epochs,
overfitting, and generalizing. The joke turns on overfitting — a model that
has memorized one thing so completely it cannot generalize to anything
else — which, as a love line, means: I could only ever fall for you.
"""

LINE = (
    "I overfit on you after a single epoch, "
    "and I've never been happier to fail to generalize."
)


def main() -> None:
    import os

    # The gate allows 1 to 200 characters; refuse to emit an overlong line
    # rather than silently submitting an invalid entry.
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
