import pytest

from adventofcode_2023.day_02 import cube_condurum, parse_game_data, cube_power


@pytest.mark.parametrize(
    "game_data, expected_result",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
         (1, [{"r": 4, "g": 0, "b": 3}, {"r": 1, "g": 2, "b": 6},
          {"r": 0, "g": 2, "b": 0}])
         ),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
         (2, [{"r": 0, "g": 2, "b": 1}, {"r": 1, "g": 3, "b": 4},
          {"r": 0, "g": 1, "b": 1}])),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, "
         "1 red",
         (3, [{"r": 20, "g": 8, "b": 6}, {"r": 4, "g": 13, "b": 5},
          {"r": 1, "g": 5, "b": 0}])
         ),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, "
         "14 red",
         (4, [{"r": 3, "g": 1, "b": 6}, {"r": 6, "g": 3, "b": 0},
          {"r": 14, "g": 3, "b": 15}])),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
         (5, [{"r": 6, "g": 3, "b": 1}, {"r": 1, "g": 2, "b": 2}]))
    ]
)
def test_parse_game_data(game_data, expected_result):
    assert parse_game_data(game_data) == expected_result


def test_cube_condurum_example() -> None:
    in_str = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert cube_condurum(in_str) == 8


def test_cube_power_example() -> None:
    in_str = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert cube_power(in_str) == 2286
