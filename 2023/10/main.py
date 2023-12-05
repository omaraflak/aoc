RangeMap = tuple[int, int, int]
Range = tuple[int, int]


def get_overlap_and_non_overlap(t1: int, t2: int, s1: int, s2: int) -> tuple[Range, list[Range]]:
    start = max(t1, s1)
    end = min(t2, s2)

    if start >= end:
        return (None, [])

    if t1 <= s1 and t2 >= s2:
        return ((start, end), [])

    if s1 <= t1 and s2 >= t2:
        return ((start, end), [(s1, t1), (t2, s2)])

    non_overlap = (s1, t1) if start == t1 else (t2, s2)
    return ((start, end), [non_overlap])



def map_range(_range: RangeMap, map: list[RangeMap], result: list[RangeMap] = None) -> list[RangeMap]:
    result = result or []
    x2, l2 = _range
    for y1, x1, l1 in map:
        overlap, non_overlaps = get_overlap_and_non_overlap(x1, x1 + l1, x2, x2 + l2)
        if not overlap and not non_overlaps:
            continue

        m, n = overlap
        mapped_overlap = (m + (y1 - x1), n - m)
        result.append(mapped_overlap)

        for non_overlap in non_overlaps:
            m, n = non_overlap
            result.extend(map_range((m, n - m), map, result))

        return result

    return [_range]
        


with open('10/input.txt', 'r') as file:
    lines = file.readlines()
    seeds = [int(x) for x in lines[0].split(': ')[1].strip('\n').split(' ')]
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    i = 3
    map: list[RangeMap] = list()
    while i < len(lines):
        map.clear()
        while i < len(lines) and lines[i] != '\n':
            dest, source, length = lines[i].strip('\n').split()
            map.append((int(dest), int(source), int(length)))
            i += 1

        seeds = list({
            _range_out
            for _range_in in seeds
            for _range_out in map_range(_range_in, map)
        })
        i += 2

    print(min(r[0] for r in seeds))