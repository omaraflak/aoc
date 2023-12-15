def read_file() -> list[str]:
    with open('input.txt', 'r') as file:
        return file.read().strip('\n').split(',')


def hash_string(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def focus_power(instructions: list[str]) -> int:
    boxes: list[dict[str, int]] = [dict() for _ in range(256)]
    for ins in instructions:
        if ins[-1] == '-':
            label = ins[:-1]
            box = hash_string(label)
            if label in boxes[box]:
                del boxes[box][label]
        else:
            label, num = ins.split('=')
            box = hash_string(label)
            boxes[box][label] = int(num)
    
    result = 0
    for box, lens in enumerate(boxes, start=1):
        for slot, length in enumerate(lens.values(), start=1):
            result += box * slot * length
    return result


def solve():
    lines = read_file()
    part1 = sum(hash_string(s) for s in lines)
    part2 = focus_power(lines)
    assert part1 == 517315
    assert part2 == 247763
    print('part1:', part1)
    print('part2:', part2)


solve()
