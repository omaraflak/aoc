RGB = tuple[int, int, int]

def read_input() -> dict[int, list[RGB]]:
    result: dict[int, list[RGB]] = dict()
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            game, nums = line.strip('\n').split(': ')
            game_num = game.split(' ')[1]
            rgb_list = []    
            for rgb in nums.split('; '):
                red, green, blue = 0, 0, 0
                for c in rgb.split(', '):
                    number, color = c.split(' ')
                    if color == 'red':
                        red = int(number)
                    if color == 'green':
                        green = int(number)
                    if color == 'blue':
                        blue = int(number)
                rgb_list.append((red, green, blue))
            result[int(game_num)] = rgb_list
        return result


def is_possible(rgb: RGB) -> bool:
    red, green, blue = rgb
    return red <= 12 and green <= 13 and blue <= 14


possible_games_sum = 0
for game, draws in read_input().items():
    if all(is_possible(draw) for draw in draws):
        possible_games_sum += game

print(possible_games_sum)