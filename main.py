# "The joke about the demo" — entry for make.fun bounty
# the-joke-about-the-demo-20261123-0112
#
# A one-line joke about working beside AI coding agents.
#
# The joke lands on a reversal: when the live demo crashes, the
# agent does not blame the code, the Wi-Fi, or itself — it files
# a bug report against the audience, for asking a question that
# was not in the script. That is the demo truth every developer
# recognises at once: an agent is flawless on script, and brittle
# the moment a real person goes off script.
#
# This program only hands the joke to the grader: it writes the
# exact text below to /output/entry.txt, UTF-8, one line.
# No network, no clock, no files outside the repository; both
# grader runs must write the same bytes, so this is a plain,
# deterministic write.
#
# Run locally the way the grader does:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = (
    "My AI agent crashed the demo live, then filed a bug report "
    "against the audience for asking an unscripted question."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    output = Path(OUTPUT_DIR) / "entry.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 280, f"joke is {len(text)} characters"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be one line"
    output.write_text(text, encoding="utf-8")
    os.chmod(output, 0o644)


if __name__ == "__main__":
    main()
