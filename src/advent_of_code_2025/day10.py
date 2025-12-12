import ast
import re
from collections import deque
from collections.abc import Generator
from pathlib import Path

cwd = Path(__file__).parent
file = cwd / "inputs/day10.txt"

PAT = re.compile(
    r"^\s*"
    r"\[([^\]]*)\]"
    r"\s*"
    r"((?:\(\s*\d+\s*(?:,\s*\d+\s*)*\)\s*)+)"
    r"\s*"
    r"\{([^}]*)\}"
    r"\s*$"
)


def extract_lines(file_path) -> Generator[tuple[str, str, str]]:
    with open(file_path) as f:
        for line in f:
            match = PAT.match(line.strip())
            if match:
                diagram, buttons, joltage = match.groups()
                yield diagram, buttons, joltage


def diagram_to_bin(diagram: str) -> int:
    chars = [c for c in diagram if c in ".#"]
    bits = "".join("1" if c == "#" else "0" for c in chars)
    return int(bits, 2) if bits else 0


def to_tuple(x):
    v = ast.literal_eval(x)
    return v if isinstance(v, tuple) else (v,)


def tuple_to_bin(positions: tuple[int, ...], width: int) -> int:
    pos_set = set(positions)
    bits = "".join("1" if i in pos_set else "0" for i in range(0, width))
    return int(bits, 2)


def parse_buttons(btn_string: str, pad: int) -> list[int]:
    btn_list = [to_tuple(btns) for btns in btn_string.split()]
    return [tuple_to_bin(btns, pad) for btns in btn_list]


def day10_01(file):
    q = deque()
    total = 0

    for line in extract_lines(file):
        diagram, buttons, _ = line
        diagram_bits = diagram_to_bin(diagram)
        padding = len(diagram)
        btn_list = parse_buttons(buttons, padding)
        q.clear()
        q.append((0, 0, 0))  # prev, next, count
        seen = set()

        while q:
            prev, btns, count = q.popleft()
            if (prev, btns) in seen:
                continue
            else:
                seen.add((prev, btns))

            state = prev ^ btns

            if state == diagram_bits:
                total += count
                break

            prev = state
            count += 1
            for btn in btn_list:
                q.append((prev, btn, count))

    return total


print(day10_01(file))
