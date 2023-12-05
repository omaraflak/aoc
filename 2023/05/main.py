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


sum_of_parts = 0
for i, line in enumerate(lines):
    start = -1
    for j, c in enumerate(line):
        if '0' <= c <= '9':
            if start == -1:
                start = j
        elif start != -1:
            if is_part(i, start, j):
                sum_of_parts += int(line[start : j])
            start = -1

print(sum_of_parts)