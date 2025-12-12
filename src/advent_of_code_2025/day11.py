from collections import deque
from collections.abc import Generator
from pathlib import Path

cwd = Path(__file__).parent
file = cwd / "inputs/day11.txt"


def extract_points(file_path) -> Generator[tuple[str, str]]:
    with open(file_path) as f:
        for line in f:
            x, y = line.strip().split(":")
            yield x, y


def day11_01(file):
    tree = {}
    for line in extract_points(file):
        dev, conn = line
        conns = conn.split() if isinstance(conn.split(), list) else [conn]
        tree[dev] = conns

    q = deque()
    for con in tree["you"]:
        q.append(con)

    seen = set()

    total = 0

    while q:
        con = q.popleft()

        if con in seen:
            total += 1
            continue

        if con == "out":
            total += 1
            continue

        for nxt in tree[con]:
            q.append(nxt)

    return total


print(day11_01(file))
