def find_last(nums: list[int]) -> int:
    result = nums[-1]
    while not all(x == 0 for x in nums):
        nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        result += nums[-1]
    return result


with open('input.txt', 'r') as file:
    result = 0
    for line in file.readlines():
        nums = [int(x) for x in line.split()]
        result += find_last(nums)
    print(result)