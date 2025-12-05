def neighbours8(row: int, col: int):
    for delta_row in (-1, 0, 1):
        for delta_col in (-1, 0, 1):
            if delta_row == 0 and delta_col == 0:
                continue
            yield row + delta_row, col + delta_col


test = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip().split("\n")

with open("./inputs/day04.txt") as file:
    input = file.readlines()


def day04_part01(input):
    row_limit = len(input)
    col_limit = len(input[0].strip())
    count = 0
    for r, row in enumerate(input):
        for c, col in enumerate(row):
            if input[r][c] == "@":
                pos_count = 0
                for test_row, test_col in neighbours8(r, c):
                    if (
                        0 <= test_row < row_limit
                        and 0 <= test_col < col_limit
                        and input[test_row][test_col] == "@"
                    ):
                        pos_count += 1
                count += 1 if pos_count < 4 else 0
    return count


def day04_part02(input):
    row_limit = len(input)
    col_limit = len(input[0].strip())
    removed: set[tuple[int, int]] = set()
    added = -1
    while added != 0:
        start_length = len(removed)
        for r, row in enumerate(input):
            for c, col in enumerate(row):
                if input[r][c] == "@" and (r, c) not in removed:
                    pos_count = 0
                    for test_row, test_col in neighbours8(r, c):
                        if (
                            0 <= test_row < row_limit
                            and 0 <= test_col < col_limit
                            and (test_row, test_col) not in removed
                            and input[test_row][test_col] == "@"
                        ):
                            pos_count += 1
                    if pos_count < 4:
                        removed.add((r, c))
        added = len(removed) - start_length
    return len(removed)


print(day04_part01(input))

print(day04_part02(input))
