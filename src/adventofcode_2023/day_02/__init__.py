def parse_game_data(game_str: str) -> tuple[int, list[dict]]:
    game, sets_data = game_str.split(':')
    game_id = int(game.split(" ")[1])
    sets_strs = sets_data.split(';')
    sets_strs = [s.split(",") for s in sets_strs]
    sets = []

    for s in sets_strs:
        set_result = {"r": 0, "g": 0, "b": 0}
        for v in [cubes.split() for cubes in s]:
            set_result[v[1][0]] = int(v[0])
        sets.append(set_result)
    return game_id, sets


def cube_condurum(input_string: str) -> int:
    games = [
        parse_game_data(game_str) for game_str in input_string.splitlines()
    ]
    sum_ = 0
    for id_, sets in games:
        possible = True
        for set_ in sets:
            if set_["r"] > 12 or set_["g"] > 13 or set_["b"] > 14:
                possible = False
        sum_ += id_ if possible else 0

    return sum_


if __name__ == '__main__':
    with open("my_input", "r") as f:
        my_input = f.read()

    print(cube_condurum(my_input))
