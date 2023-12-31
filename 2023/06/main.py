from math import sqrt, floor, ceil, prod


def solve(t: int, d: int) -> int:
    x1 = (t - sqrt(t * t - 4 * d)) / 2
    x2 = (t + sqrt(t * t - 4 * d)) / 2
    x1 = x1 + 1 if int(x1) == x1 else x1
    x2 = x2 - 1 if int(x2) == x2 else x2
    return floor(x2) - ceil(x1) + 1


inputs = [(40, 215), (70, 1051), (98, 2147), (79, 1005)]

result1 = prod(solve(t, d) for t, d in inputs)
result2 = solve(40709879, 215105121471005)

assert result1 == 1084752
assert result2 == 28228952
print('part 1:', result1)
print('part 2:', result2)
