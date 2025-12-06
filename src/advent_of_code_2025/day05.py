from collections.abc import Generator
from pathlib import Path

cwd = Path(__file__).parent
file = cwd / "inputs/day05.txt"


def extract_lines(file_path) -> Generator[str]:
    with open(file) as f:
        for line in f:
            yield line.strip()


def day05_part01(file: Path) -> int:
    is_range = True
    ranges = set()
    count = 0
    for line in extract_lines(file):
        if line == "":
            is_range = False
            continue
        if is_range:
            ranges.add(line)
        else:
            for rang in ranges:
                left, right = map(int, rang.split("-"))
                if left <= int(line) <= right:
                    count += 1
                    break
    return count


def day05_part02(file: Path) -> int:
    ranges = []
    for line in extract_lines(file):
        if line == "":
            break
        ranges.append(tuple(map(int, line.split("-"))))
    ranges = sorted(ranges, key=lambda x: (x[0], x[1]))
    count = 0
    left, right = ranges[0]
    for next_left, next_right in ranges[1:]:
        if right >= next_left:
            right = max(next_right, right)
            continue
        count += right - left + 1
        left, right = next_left, next_right
    count += right - left + 1
    return count


print(day05_part01(file))
print(day05_part02(file))
