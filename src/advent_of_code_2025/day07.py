from collections.abc import Generator
from pathlib import Path

cwd = Path(__file__).parent
file = cwd / "inputs/day07.txt"


def extract_lines(file_path) -> Generator[str]:
    with open(file_path) as f:
        for line in f:
            yield line.strip()


def day07_01(file):
    generator = extract_lines(file)
    start_line = next(generator)
    max_index = len(start_line)
    beam_index = {start_line.index("S")}

    splits = 0

    for line in generator:
        line_splitters = set()
        for i, char in enumerate(line):
            if char == "^":
                line_splitters.add(i)
        splitters = line_splitters & beam_index
        splits += len(splitters)
        new_beams = set()
        for split in splitters:
            left = max(0, split - 1)
            right = min(max_index, split + 1)
            new_beams.update({left, right})
        beam_index -= splitters
        beam_index |= new_beams

    return splits


print(day07_01(file))
