import math
import re


with open('input.txt', 'r') as file:
    path = list(file.readline().strip('\n'))
    graph: dict[str, tuple[str, str]] = dict()
    pattern = re.compile(r'(.*) = \((.*), (.*)\)')
    for line in file.readlines():
        for a, b, c in pattern.findall(line):
            graph[a] = (b, c)


def count_steps(key: str) -> int:
    count = 0
    while key[-1] != 'Z':
        dir = path[count % len(path)]
        dir = 0 if dir == 'L' else 1
        key = graph[key][dir]
        count += 1
    return count

steps = [count_steps(key) for key in graph if key[-1] == 'A']
result = math.lcm(*steps)
print(result)