from collections import Counter


order = {
    'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6,
    '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12
}


def hand_key(hand: str) -> tuple[int,...]:
    counts = Counter(hand)
    values = set(counts.values())

    # five of a kind
    if len(counts) == 1:
        hand_type = 0

    # four of a kind
    elif len(counts) == 2 and 4 in values:
        hand_type = 1

    # full house
    elif len(counts) == 2 and 3 in values:
        hand_type = 2

    # three of a kind
    elif len(counts) == 3 and 3 in values:
        hand_type = 3

    # two pair
    elif sorted(counts.values()) == [1, 2, 2]:
        hand_type = 4

    # one pair
    elif  len(counts) == 4:
        hand_type = 5

    # high card
    elif len(counts) == 5:
        hand_type = 6

    else:
        raise RuntimeError()

    vals = tuple(order[c] for c in hand)
    return (hand_type,) + vals


with open('input.txt', 'r') as file:
    hands = [line.split() for line in file.readlines()]
    hands = [(x, int(y)) for x, y in hands]
    result = sum(
        hand[1] * (i + 1)
        for i, hand in enumerate(reversed(sorted(hands, key=lambda x: hand_key(x[0]))))
    )
    print(result)

