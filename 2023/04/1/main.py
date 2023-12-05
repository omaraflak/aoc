with open('input.txt', 'r') as file:
    total_points = 0
    for line in file.readlines():
        winning, numbers = line.split(':')[1].split('|')
        winning = {int(n.strip()) for n in winning.split(' ') if n != ''}
        numbers = {int(n.strip()) for n in numbers.split(' ') if n != ''}
        points = sum(1 for n in winning if n in numbers)
        if points > 0:
            total_points += 1 << (points - 1)
    print(total_points)
