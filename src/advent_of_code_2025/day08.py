import math
from collections.abc import Generator
from functools import reduce
from pathlib import Path

cwd = Path(__file__).parent
file = cwd / "inputs/day08.txt"


def extract_points(file_path) -> Generator[tuple[int, int, int]]:
    with open(file_path) as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            yield x, y, z


points = []
distances = []
for point in extract_points(file):
    next_i = len(points)
    for counts, p2 in enumerate(points):
        dist = math.dist(point, p2)
        distances.append((dist, counts, next_i))
    points.append(point)

distances.sort(key=lambda x: x[0])

circuits = []
connections = 1000
for i in range(connections):
    _, i_p1, i_p2 = distances[i]
    merge = []

    for c, circuit in enumerate(circuits):
        if i_p1 in circuit and i_p2 in circuit:
            break
        if i_p1 in circuit or i_p2 in circuit:
            merge.append(c)

    if merge:
        to_merge = [circuits[x] for x in merge]
        circuits = [circuit for i, circuit in enumerate(circuits) if i not in merge]
        merged = {i_p1, i_p2}
        merged.update(*to_merge)
        circuits.append(merged)
    else:
        circuits.append({i_p1, i_p2})

circuits.sort(key=lambda x: len(x), reverse=True)
firsts = circuits[:3]
print(math.prod(len(cir) for cir in firsts))

# 2548 too low
