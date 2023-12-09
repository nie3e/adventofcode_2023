import pytest

from adventofcode_2023.day_03 import (gear_ratios, get_numbers, get_symbols,
                                      Number, Symbol)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("467..114..", [Number(467, 0, 2, 1), Number(114, 5, 7, 1)]),
        ("...*......", []),
        ("..35..633.", [Number(35, 2, 3, 1), Number(633, 6, 8, 1)]),
        ("......#...", []),
        ("617*......", [Number(617, 0, 2, 1)]),
        (".....+.58.", [Number(58, 7, 8, 1)]),
        ("..592.....", [Number(592, 2, 4, 1)]),
        ("......755.", [Number(755, 6, 8, 1)]),
        ("...$.*....", []),
        (".664.598..", [Number(664, 1, 3, 1), Number(598, 5, 7, 1)]),
    ]
)
def test_get_numbers(test_input, expected):
    assert get_numbers(test_input, 1) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("467..114..", []),
        ("...*......", [Symbol(3, 1)]),
        ("..35..633.", []),
        ("......#...", [Symbol(6, 1)]),
        ("617*......", [Symbol(3, 1)]),
        (".....+.58.", [Symbol(5, 1)]),
        ("..592.....", []),
        ("......755.", []),
        ("...$.*....", [Symbol(3, 1), Symbol(5, 1)]),
        (".664.598..", []),
    ]
)
def test_get_symbols(test_input, expected):
    assert get_symbols(test_input, 1) == expected


@pytest.mark.parametrize(
    "number, sumbol, expected",
    [
        (Number(467, 0, 2, 1), Symbol(3, 1), True),
        (Number(114, 5, 7, 1), Symbol(3, 1), False),
        (Number(58, 7, 8, 5), Symbol(5, 5), False)
    ]
)
def test_number_is_touching_symbol(number, sumbol, expected):
    assert number.is_touching(sumbol) == expected


def test_gear_ratios_example():
    input_string = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert gear_ratios(input_string) == (4361, 467835)
