with open('input.txt', 'r') as file:
    s = 0
    for line in file.readlines():
        first = -1
        last = -1
        for c in line:
            if '0' <= c <= '9':
                p = ord(c) - ord('0')
                if first == -1:
                    first = p
                last = p
        s += first * 10 + last

    assert s == 54338
    print(s)