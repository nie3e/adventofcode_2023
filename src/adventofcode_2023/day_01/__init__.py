"""https://adventofcode.com/2023/day/1"""
from typing import Optional


def find_first_digit_in_string(in_: str) -> Optional[int]:
    for c in in_:
        if c.isdigit():
            return int(c)
    return None


def trebuchet(input_string: str) -> int:
    input_sum = 0
    for line in input_string.splitlines():
        input_sum += (find_first_digit_in_string(line) * 10 +
                find_first_digit_in_string(line[::-1]))
    return input_sum


if __name__ == '__main__':
    with open("my_input", "r") as f:
        my_input = f.read()

    print(trebuchet(my_input))
