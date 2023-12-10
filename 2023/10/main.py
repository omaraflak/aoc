Node = tuple[int, int]

valid_neighbors = {
    # top, left, bottom, right
    'S': [{'|', '7', 'F'}, {'-', 'F', 'L'}, {'|', 'J', 'L'}, {'-', '7', 'J'}],
    '-': [{}, {'-', 'F', 'L'}, {}, {'-', '7', 'J'}],
    '|': [{'|', '7', 'F'}, {}, {'|', 'L', 'J'}, {}],
    '7': [{}, {'-', 'F', 'L'}, {'|', 'L', 'J'}, {}],
    'J': [{'|', '7', 'F'}, {'-', 'F', 'L'}, {}, {}],
    'F': [{}, {}, {'|', 'L', 'J'}, {'-', 'J', '7'}],
    'L': [{'|', '7', 'F'}, {}, {}, {'-', 'J', '7'}],
}


def read_input() -> list[str]:
    with open('input.txt', 'r') as file:
        return [line.strip('\n') for line in file.readlines()]


def find_start(lines: list[str]) -> Node:
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                return (i, j)


def get_valid_neighbors(lines: list[str], node: Node) -> list[Node]:
    result: list[Node] = list()
    m, n = node
    char = lines[m][n]
    if m - 1 >= 0 and lines[m - 1][n] in valid_neighbors[char][0]:
        result.append((m - 1, n))
    if n - 1 >= 0 and lines[m][n - 1] in valid_neighbors[char][1]:
        result.append((m, n - 1))
    if m + 1 < len(lines) and lines[m + 1][n] in valid_neighbors[char][2]:
        result.append((m + 1, n))
    if n + 1 < len(lines[m]) and lines[m][n + 1] in valid_neighbors[char][3]:
        result.append((m, n + 1))
    return result


def get_loop_nodes(lines: list[str]) -> set[Node]:
    loop: set[Node] = set()
    queue = [find_start(lines)]
    while queue:
        node = queue.pop()
        if node in loop:
            continue

        loop.add(node)
        for neighbor in get_valid_neighbors(lines, node):
            if neighbor not in loop:
                queue.append(neighbor)

    return loop


def is_in_loop(lines: list[str], loop: set[Node], i: int, j: int) -> bool:
    count = 0
    prev = ''
    while j >= 0:
        if (i, j) in loop:
            if lines[i][j] in {'J', '7'}:
                prev = lines[i][j]
            elif lines[i][j] == 'F' and prev == 'J':
                count += 1
            elif lines[i][j] == 'L' and prev == '7':
                count += 1
            elif lines[i][j] == '|':
                count += 1
        j -= 1
    return count % 2 == 1


def count_enclosed_tiles(lines: list[str], loop: set[Node]) -> int:
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i, j) not in loop and is_in_loop(lines, loop, i, j):
                count += 1
    return count


lines = read_input()
loop = get_loop_nodes(lines)
max_dist = len(loop) // 2
tiles = count_enclosed_tiles(lines, loop)

assert max_dist == 6842
assert tiles == 393

print('part1:', max_dist)
print('part2:', tiles)