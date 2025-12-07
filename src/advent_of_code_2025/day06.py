from collections.abc import Generator
from pathlib import Path

import numpy as np

cwd = Path(__file__).parent
file = cwd / "inputs/day06.txt"


def extract_lines(file_path) -> Generator[str]:
    with open(file_path) as f:
        for line in f:
            yield line


def day06_01(line_generator: Generator[str]) -> int:
    matrix = []
    for line in line_generator:
        matrix.append(line.split())

    operations = matrix.pop(-1)
    array = np.array(matrix, dtype=int)

    reducers = {"+": np.sum, "*": np.prod}

    res = np.empty(array.shape[1], dtype=array.dtype)
    for j, op in enumerate(operations):
        res[j] = reducers[op](array[:, j])

    return np.sum(res)


print(day06_01(extract_lines(file)))
