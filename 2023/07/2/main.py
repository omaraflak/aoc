from collections import Counter


order = {
    '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
    'T': 8, 'J': -1, 'Q': 10, 'K': 11, 'A': 12,
}


def hand_key(hand: str) -> tuple[int,...]:
    counts = Counter(hand)

    if 'J' in counts:
        # find the strongest most present card that's not a J
        comp = lambda x: (0 if x[0] == 'J' else x[1], order[x[0]])
        max_card, _ = max(counts.items(), key=comp)
        # if the hand has only Js, then max_card will be J any ways...
        if max_card == 'J':
            max_card = 'A'
        counts[max_card] += counts['J']
        del counts['J']
    
    values = set(counts.values())
    unique_cards = len(counts)

    # five of a kind
    if unique_cards == 1:
        hand_type = 6

    # four of a kind
    elif unique_cards == 2 and 4 in values:
        hand_type = 5

    # full house
    elif unique_cards == 2 and 3 in values:
        hand_type = 4

    # three of a kind
    elif unique_cards == 3 and 3 in values:
        hand_type = 3

    # two pair
    elif sorted(counts.values()) == [1, 2, 2]:
        hand_type = 2

    # one pair
    elif  unique_cards == 4:
        hand_type = 1

    # high card
    elif unique_cards == 5:
        hand_type = 0

    else:
        raise RuntimeError()

    vals = tuple(order[c] for c in hand)
    return (hand_type,) + vals


with open('input.txt', 'r') as file:
    hands = [line.split() for line in file.readlines()]
    hands = [(x, int(y)) for x, y in hands]
    hands.sort(key=lambda x: hand_key(x[0]))
    result = sum(hand[1] * i for i, hand in enumerate(hands, start=1))
    print(result)
