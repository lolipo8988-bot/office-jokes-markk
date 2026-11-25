"""One-Line Office Jokes entry.

Writes a single one-line office joke to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 199 characters,
not only white space, on a single line. The program is
deterministic: every run writes exactly the same bytes.

The joke is assembled from its two beats so the structure mirrors
how it lands: a familiar office setup (the meeting that should
have been an email) and the turn saved for the final words
(attending as an out-of-office reply).

For local verification only, the output path can be redirected
with the ENTRY_OUTPUT_PATH environment variable; the grader
runs it with no override, so it writes to /output/entry.txt.
"""

import os

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199

SETUP = "My boss said this meeting could have been an email, so I attended it as"
PUNCHLINE = "an out-of-office reply."


def build_joke() -> str:
    """Join the setup and the punchline into one single line."""
    return f"{SETUP} {PUNCHLINE}"


def validate(text: str) -> str:
    """Return the entry text, or raise if it would fail the gate."""
    cleaned = text.strip()
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if not cleaned:
        raise ValueError("entry must not be only white space")
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(cleaned)}")
    return cleaned


def main() -> None:
    text = validate(build_joke())
    output_path = os.environ.get("ENTRY_OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
