from typing import Iterator


Pos = tuple[int, int]
Dir = Pos


def read_file() -> list[str]:
    with open('input.txt', 'r') as file:
        return [line.strip('\n') for line in file.readlines()]


def count_energised(lines: list[str], start_pos: Pos, start_dir: Dir) -> int:
    beams: list[tuple[Pos, Dir]] = [(start_pos, start_dir)]
    seen: set[tuple[Pos, Dir]] = set()
    energised: set[Pos] = set()
    while beams:
        to_remove: list[tuple[Pos, Dir]] = list()
        to_add: list[tuple[Pos, Dir]] = list()
        
        for idx, beam in enumerate(beams):
            if beam in seen:
                to_remove.append(beam)
                continue
                
            seen.add(beam)

            (i, j), (m, n) = beam
            if not (0 <= i < len(lines) and 0 <= j < len(lines[0])):
                to_remove.append(beam)
                continue

            energised.add((i, j))

            if lines[i][j] == '.':
                beams[idx] = ((i + m, j + n), (m, n))
            elif lines[i][j] == '-':
                if n == 1 or n == -1:
                    beams[idx] = ((i + m, j + n), (m, n))
                else:
                    to_remove.append(beam)
                    to_add.append(((i, j + 1), (0, 1)))
                    to_add.append(((i, j - 1), (0, -1)))
            elif lines[i][j] == '|':
                if m == 1 or m == -1:
                    beams[idx] = ((i + m, j + n), (m, n))
                else:
                    to_remove.append(beam)
                    to_add.append(((i + 1, j), (1, 0)))
                    to_add.append(((i - 1, j), (-1, 0)))
            elif lines[i][j] == '/':
                if (m, n) == (0, 1):
                    beams[idx] = ((i - 1, j), (-1, 0))
                elif (m, n) == (0, -1):
                    beams[idx] = ((i + 1, j), (1, 0))
                elif (m, n) == (1, 0):
                    beams[idx] = ((i, j - 1), (0, -1))
                else:
                    beams[idx] = ((i, j + 1), (0, 1))
            elif lines[i][j] == '\\':
                if (m, n) == (0, 1):
                    beams[idx] = ((i + 1, j), (1, 0))
                elif (m, n) == (0, -1):
                    beams[idx] = ((i - 1, j), (-1, 0))
                elif (m, n) == (1, 0):
                    beams[idx] = ((i, j + 1), (0, 1))
                else:
                    beams[idx] = ((i, j - 1), (0, -1))

        for beam in to_remove:
            beams.remove(beam)

        for beam in to_add:
            beams.append(beam)

        to_remove.clear()
        to_add.clear()

    return len(energised)


def all_beams(height: int, width: int) -> Iterator[tuple[Pos, Dir]]:
    for i in range(height):
        yield ((i, 0), (0, 1))
        yield ((i, width - 1), (0, -1))

    for j in range(width):
        yield ((0, j), (1, 0))
        yield ((height - 1, j), (-1, 0))


def solve():
    lines = read_file()
    part1 = count_energised(lines, (0, 0), (0, 1))
    part2 = max(
        count_energised(lines, pos, dir)
        for pos, dir in all_beams(len(lines), len(lines[0]))
    )
    assert part1 == 7788
    assert part2 == 7987
    print('part1:', part1)
    print('part2:', part2)


solve()
