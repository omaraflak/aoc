import re


with open('input.txt', 'r') as file:
    path = list(file.readline().strip('\n'))
    graph: dict[str, tuple[str, str]] = dict()
    pattern = re.compile(r'(.*) = \((.*), (.*)\)')
    for line in file.readlines():
        for a, b, c in pattern.findall(line):
            graph[a] = (b, c)

    count = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        dir = path[count % len(path)]
        dir = 0 if dir == 'L' else 1
        curr = graph[curr][dir]
        count += 1

    print(count)
