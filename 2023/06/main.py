from collections import defaultdict


with open('input.txt', 'r') as file:
    lines = file.readlines()


def is_symbol(c: str) -> bool:
    return not (c == '.' or c == '\n' or '0' <= c <= '9')


def is_part(line: int, start: int, stop: int) -> bool:
    for i in range(line - 1, line + 2):
        for j in range(start - 1, stop + 1):
            if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
                if is_symbol(lines[i][j]):
                    return True
    return False


def get_gears(line: int, start: int, stop: int) -> list[tuple[int, int]]:
    gears = []
    for i in range(line - 1, line + 2):
        for j in range(start - 1, stop + 1):
            if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
                if lines[i][j] == '*':
                    gears.append((i, j))
    return gears


gears: dict[tuple[int, int], list[int]] = defaultdict(list)
for i, line in enumerate(lines):
    start = -1
    for j, c in enumerate(line):
        if '0' <= c <= '9':
            if start == -1:
                start = j
        elif start != -1:
            if is_part(i, start, j):
                for m, n in get_gears(i, start, j):
                    gears[(m, n)].append(int(line[start : j]))
            start = -1


sum_of_gear_ratios = 0
for nums in gears.values():
    if len(nums) == 2:
        sum_of_gear_ratios += nums[0] * nums[1]

print(sum_of_gear_ratios)