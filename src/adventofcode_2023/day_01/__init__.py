"""https://adventofcode.com/2023/day/1"""
from typing import Optional
import re

words = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
         "8": 8, "9": 9, "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
         "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def first_last_digit_in_string(in_: str) -> Optional[tuple[int, int]]:
    to_find = "|".join(words.keys())
    matches = re.findall(f"(?=({to_find}))", in_)
    if not matches:
        return None
    return words[matches[0]], words[matches[-1]]


def trebuchet(input_string: str) -> int:
    input_sum = 0
    for line in input_string.splitlines():
        first, last = first_last_digit_in_string(line)
        input_sum += first * 10 + last
    return input_sum


if __name__ == '__main__':
    with open("my_input", "r") as f:
        my_input = f.read()

    print(trebuchet(my_input))
