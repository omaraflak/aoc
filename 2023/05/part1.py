Range = tuple[int, int, int]


def map_number(n: int, maps: list[Range]) -> int:
    for dest, source, length in maps:
        if source <= n < source + length:
            return dest + (n - source)
    return n


with open('input.txt', 'r') as file:
    lines = file.readlines()
    seeds = [int(x) for x in lines[0].split(': ')[1].strip('\n').split(' ')]

    i = 3
    maps: list[Range] = list()
    while i < len(lines):
        maps.clear()
        while i < len(lines) and lines[i] != '\n':
            dest, source, length = lines[i].strip('\n').split()
            maps.append((int(dest), int(source), int(length)))
            i += 1

        seeds = [map_number(n, maps) for n in seeds]
        i += 2

    result = min(seeds)

    assert result == 214922730
    print(result)