def find_first(nums: list[int]) -> int:
    result = nums[0]
    i = -1
    while not all(x == 0 for x in nums):
        nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        result += i * nums[0]
        i *= -1
    return result


with open('input.txt', 'r') as file:
    result = 0
    for line in file.readlines():
        nums = [int(x) for x in line.split()]
        result += find_first(nums)
    print(result)