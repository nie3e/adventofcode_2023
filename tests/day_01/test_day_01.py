import pytest
from adventofcode_2023.day_01 import trebuchet, find_first_digit_in_string


@pytest.mark.parametrize(
    "test_input, expected",
    (("1abc2", 1), ("pqr3stu8vwx", 3), ("a1b2c3d4e5f", 1), ("treb7uchet", 7))
)
def test_find_first_digit_in_string(test_input, expected) -> None:
    assert find_first_digit_in_string(test_input) == expected


def test_trebuchet_example() -> None:
    in_str = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert trebuchet(in_str) == 142
