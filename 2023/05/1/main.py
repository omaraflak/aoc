Range = tuple[int, int, int]


def map_number(n: int, map: list[Range]) -> int:
    for dest, source, length in map:
        if source <= n < source + length:
            return dest + (n - source)
    return n


with open('input.txt', 'r') as file:
    lines = file.readlines()
    seeds = [int(x) for x in lines[0].split(': ')[1].strip('\n').split(' ')]
    map: list[Range] = list()

    i = 3
    while i < len(lines):
        map.clear()
        while i < len(lines) and lines[i] != '\n':
            dest, source, length = lines[i].strip('\n').split()
            map.append((int(dest), int(source), int(length)))
            i += 1

        seeds = [map_number(n, map) for n in seeds]
        i += 2

    print(min(seeds))