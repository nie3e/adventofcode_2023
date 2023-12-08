import pytest
from adventofcode_2023.day_01 import trebuchet, first_last_digit_in_string


@pytest.mark.parametrize(
    "test_input, expected",
    (("1abc2", (1, 2)), ("pqr3stu8vwx", (3, 8)), ("a1b2c3d4e5f", (1, 5)),
     ("treb7uchet", (7, 7)), ("two1nine", (2, 9)), ("eightwothree", (8, 3)),
     ("abcone2threexyz", (1, 3)), ("xtwone3four", (2, 4)),
     ("4nineeightseven2", (4, 2)), ("zoneight234", (1, 4)),
     ("7pqrstsixteen", (7, 6)), ("4nineeight", (4, 8)),
     ("xxhmbpvr7vvppfreightthreefivefive", (7, 5)), ("eighthree", (8, 3)))
)
def test_first_last_digit_in_string(test_input, expected) -> None:
    assert first_last_digit_in_string(test_input) == expected


def test_trebuchet_example() -> None:
    in_str = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert trebuchet(in_str) == 142


def test_trebuchet_example2() -> None:
    in_str = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert trebuchet(in_str) == 281
