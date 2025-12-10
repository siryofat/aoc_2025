from collections.abc import Generator
from pathlib import Path

from shapely import LineString, Polygon

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


def line_in_polygon(pol: Polygon, line: LineString):
    return pol.covers(line)


def day09_02(file):
    points = []
    max_rect = 0
    max_p1 = ()
    max_p2 = ()
    for point in extract_points(file):
        points.append(point)
    points.append(points[0])
    polygon = Polygon(points)
    for i, p1 in enumerate(points):
        for p2 in points[i + 1 :]:
            x1, y1 = p1
            x2, y2 = p2
            side1 = LineString([(x1, y1), (x2, y1)])
            side2 = LineString([(x2, y1), (x2, y2)])
            side3 = LineString([(x2, y2), (x1, y2)])
            side4 = LineString([(x1, y2), (x1, y1)])
            if not (
                line_in_polygon(polygon, side1)
                and line_in_polygon(polygon, side2)
                and line_in_polygon(polygon, side3)
                and line_in_polygon(polygon, side4)
            ):
                continue
            d1 = abs(x1 - x2) + 1
            d2 = abs(y1 - y2) + 1
            area = d1 * d2
            max_rect = area if area > max_rect else max_rect
            if area >= max_rect:
                max_p1 = p1
                max_p2 = p2
    return max_rect, max_p1, max_p2


print(day09_01(file))
print(day09_02(file))
