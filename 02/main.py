nums = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

with open('02/input.txt', 'r') as file:
    s = 0
    for line in file.readlines():
        first_pos, first_idx = -1, -1
        last_pos, last_idx = -1, -1

        for i, n in enumerate(nums):
            pos = line.find(n)
            if pos == -1:
                continue

            if first_idx == -1 or pos < first_pos:
                first_idx = i
                first_pos = pos
            
            pos = line.rfind(n)
            if pos > last_pos:
                last_idx = i
                last_pos = pos


        if '0' <= nums[first_idx] <= '9':
            s += 10 * (first_idx - 10)
        else:
            s += 10 * first_idx
        
        if '0' <= nums[last_idx] <= '9':
            s += (last_idx - 10)
        else:
            s += last_idx
    
    print(s)
        