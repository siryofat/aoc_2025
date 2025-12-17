from collections.abc import Generator
from functools import lru_cache
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


def day07_02(file):
    lines = list(extract_lines(file))
    start = lines[0].index("S")
    rows = len(lines)
    cols = len(lines[0])

    @lru_cache(maxsize=None)
    def count_splits(r: int, c: int) -> int:
        nr = r + 1

        # base:
        if nr > rows:
            return 0

        if not (0 <= nr < rows and 0 <= c < cols):
            return 0

        pos = lines[nr][c]

        if pos == "^":
            total = 1

            left = count_splits(nr, c - 1)
            right = count_splits(nr, c + 1)

            return total + left + right
        else:
            return count_splits(nr, c)

    result = 1 + count_splits(0, start)
    return result


# print(day07_01(file))
print(day07_02(file))
