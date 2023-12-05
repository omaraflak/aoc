from collections import defaultdict

with open('08/input.txt', 'r') as file:
    cards: dict[int, int] = defaultdict(lambda: 1)
    lines = file.readlines()
    for line in lines:
        game, nums = line.split(':')
        game = int(game.split()[1].strip())
        winning, numbers = nums.split('|')
        winning = {int(n.strip()) for n in winning.split(' ') if n != ''}
        numbers = {int(n.strip()) for n in numbers.split(' ') if n != ''}
        matching = sum(1 for n in winning if n in numbers)
        for i in range(game + 1, game + 1 + matching):
            cards[i] += cards[game]

    print(sum(cards[i] for i in range(1, len(lines) + 1)))
