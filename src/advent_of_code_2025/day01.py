from collections.abc import Generator
from pathlib import Path

file = Path("./inputs/day01.txt")


def extract_lines(file_path) -> Generator[str]:
    with open(file) as f:
        for line in f:
            yield line.strip()


def get_movement(mov: str) -> tuple[str, int, int]:
    dir: str = mov[0]
    total_dist: int = int(mov[1:])
    dist = total_dist % 100
    zero_marks = int(total_dist / 100)
    return (dir, dist, zero_marks)


dial_pos = 50
pwd = 0

# for line in extract_lines(file):
for line in extract_lines(file):
    dir, dist, zero_marks = get_movement(line)
    pwd += zero_marks
    print(f"{dir=}, {dist=}")
    start = dial_pos
    if dir.lower() == "r":
        dial_pos += dist
        print(dial_pos)
    else:
        dial_pos -= dist
        print(dial_pos)

    sum = 1 if start != 0 else 0
    if dial_pos > 99:
        dial_pos -= 100
        pwd += 1
        sum = 0
    elif dial_pos < 0:
        pwd += sum
        sum = 0
        dial_pos += 100

    print(dial_pos)
    if dial_pos == 0:
        pwd += sum

    print(f"{pwd=}")

print(pwd)
