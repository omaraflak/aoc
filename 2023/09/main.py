def find_first_last(nums: list[int]) -> tuple[int, int]:
    first, last = nums[0], nums[-1]
    i = -1
    while not all(x == 0 for x in nums):
        nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        first += i * nums[0]
        last += nums[-1]
        i *= -1
    return first, last


with open('input.txt', 'r') as file:
    first, last = 0, 0
    for line in file.readlines():
        nums = [int(x) for x in line.split()]
        a, b = find_first_last(nums)
        first += a
        last += b

    assert first == 1041
    assert last == 1939607039
    print('part1:', first)
    print('part2:', last)
