import re

with open("./inputs/day02.txt") as file:
    line = file.readline()

ranges = line.split(",")

pat = re.compile(r"^(.+)\1$")
total = 0

for rang in ranges:
    first, second = rang.split("-")
    for num in range(int(first), int(second) + 1):
        num_str = str(num)
        found = pat.search(num_str)
        if found:
            total += num

print(total)
