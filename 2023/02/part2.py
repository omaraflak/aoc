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


def get_minimum_set(game: list[RGB]) -> RGB:
    red, green, blue = 0, 0, 0
    for r, g, b in game:
        red, green, blue = max(red, r), max(green, g), max(blue, b)
    return red, green, blue


def power_set(rgb: RGB) -> int:
    red, green, blue = rgb
    return red * green * blue


sum_min_set = 0
for game in read_input().values():
    sum_min_set += power_set(get_minimum_set(game))

assert sum_min_set == 70950
print(sum_min_set)