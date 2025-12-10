from collections.abc import Generator
from pathlib import Path

cwd = Path(__file__).parent
file = cwd / "inputs/day09.txt"


def extract_points(file_path) -> Generator[tuple[int, int]]:
    with open(file_path) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            yield x, y


def day09_01(file):
    coords = []
    max_area = 0
    for point in extract_points(file):
        x1, y1 = point
        for coord in coords:
            x2, y2 = coord
            d1 = abs(x1 - x2) + 1
            d2 = abs(y1 - y2) + 1
            area = d1 * d2
            max_area = area if area > max_area else max_area
        coords.append(point)
    return max_area


print(day09_01(file))
