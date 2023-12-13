def read_file() -> list[list[str]]:
    with open('input.txt', 'r') as file:
        return [lines.split('\n') for lines in file.read().split('\n\n')]


def count_diff(s1: str, s2: str) -> int:
    return sum(1 for a, b in zip(s1, s2) if a != b)


def find_symmetry(lines: list[str], diff: int) -> int:
    for i in range(1, len(lines)):
        top, down = i - 1, i
        e = 0
        while top >= 0 and down < len(lines):
            e += count_diff(lines[top], lines[down])
            top -= 1
            down += 1
        
        if e == diff:
            return i

    return 0


def score(lines: list[str], diff: int) -> int:
    i = find_symmetry(list(zip(*lines)), diff)
    j = find_symmetry(lines, diff)
    return i + 100 * j


def solve():
    lines = read_file()
    part1 = sum(score(line, 0) for line in lines)
    part2 = sum(score(line, 1) for line in lines)
    assert part1 == 35360
    assert part2 == 36755
    print('part1:', part1)
    print('part2:', part2)


solve()
