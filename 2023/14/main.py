def read_file() -> list[list[str]]:
    with open('input.txt', 'r') as file:
        return [list(line.strip('\n')) for line in file.readlines()]


def slide_north(lines: list[list[str]]) -> list[list[str]]:
    for j in range(len(lines[0])):
        c = 0
        for i in reversed(range(len(lines))):
            if lines[i][j] == 'O':
                c += 1
                lines[i][j] = '.'
            elif lines[i][j] == '#':
                for k in range(i + 1, i + 1 + c):
                    lines[k][j] = 'O'
                c = 0
        for k in range(c):
            lines[k][j] = 'O'

    return lines


def score(lines: list[list[str]]) -> int:
    return sum(l.count('O') * (len(lines) - i) for i, l in enumerate(lines))


# yak!...
def slide(lines: list[list[str]], i: int) -> list[list[str]]:
    lines = [list(x) for x in lines]

    for _ in range(i):
        lines = [list(x) for x in zip(*lines[::-1])]
    
    lines = slide_north(lines)
    
    for _ in range(i, 4):
        lines = [list(x) for x in zip(*lines[::-1])]

    return lines


def do_cycles(lines: list[list[str]], cycles: int) -> list[list[str]]:
    seen: list[list[list[str]]] = [None]
    i = 1
    while True:
        lines = slide(lines, (i - 1) % 4)
        if lines in seen:
            start_loop = seen.index(lines)
            loop_length = i - start_loop
            end_prefix = start_loop - 1
            n = end_prefix + (4 * cycles - end_prefix) % loop_length
            return seen[n]
        seen.append(lines)
        i += 1


def solve():
    lines = read_file()
    part1 = score(slide_north([list(x) for x in lines]))
    part2 = score(do_cycles(lines, 1000000000))
    assert part1 == 110128
    assert part2 == 103861
    print('part1:', part1)
    print('part2:', part2)


solve()
