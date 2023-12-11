Pos = tuple[int, int]

def read_file() -> list[str]:
    with open('input.txt', 'r') as file:
        return [line.strip('\n') for line in file.readlines()]


def count_expansions(nums: set[int], low: int, high: int) -> int:
    count = 0
    for n in nums:
        if low <= n <= high:
            count += 1
    return count


def get_expansions(lines: list[str]) -> tuple[set[int], set[int]]:
    rows: set[int] = set()
    cols: set[int] = set()

    for i, line in enumerate(lines):
        if line.count('#') == 0:
            rows.add(i)

    for j in range(len(lines[0])):
        if all(lines[i][j] == '.' for i in range(len(lines))):
            cols.add(j)

    return rows, cols


def find_galaxies(lines: list[str], scale: int) -> list[tuple[int, int]]:
    rows, cols = get_expansions(lines)
    result: list[tuple[int, int]] = list()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                di = (scale - 1) * count_expansions(rows, 0, i)
                dj = (scale - 1) * count_expansions(cols, 0, j)
                result.append((i + di, j + dj))
    return result


def shortest_path(i: int, j: int, m: int, n: int) -> int:
    return abs(i - m) + abs(j - n)


def sum_shortest_paths(positions: list[tuple[int, int]]) -> int:
    result = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            result += shortest_path(*positions[i], *positions[j])
    return result


lines = read_file()
part1 = sum_shortest_paths(find_galaxies(lines, 2))
part2 = sum_shortest_paths(find_galaxies(lines, 1000000))

assert part1 == 9274989
assert part2 == 357134560737
print(part1)
print(part2)
