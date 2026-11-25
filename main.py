from pathlib import Path

# Deterministic: same excuse every run, no randomness, no time, no extra I/O.
EXCUSE = "I missed our target window; GPU memory hit 99%, so I freed 16GB by quantizing the chat to 4-bit, which kept throughput high and rounded you to zero."


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
