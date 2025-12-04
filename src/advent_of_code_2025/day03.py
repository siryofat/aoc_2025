from collections import Counter

input = "./inputs/day03.txt"

with open(input) as f:
    lines = f.readlines()


def max_k_subsequence(s: str, k: int) -> str:
    drop = len(s) - k
    stack = []
    for ch in s:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return "".join(stack[:k])


total = 0
for line in lines:
    line = list(line.strip())
    count = Counter(line)
    for num in range(9, 1, -1):
        c = count.get(str(num), 0)
        if c > 1:
            val = str(num) * 2
            total += int(val)
            break
        elif c == 1:
            i = line.index(str(num))
            left = max(line[:i], default="")
            right = max(line[i + 1 :], default="")
            out = max(int(left + str(num)), int(str(num) + right))
            total += out
            break

print(total)

total02 = 0
for line in lines:
    max = max_k_subsequence(line.strip(), 12)
    total02 += int(max)
print(f"{total02=}")
