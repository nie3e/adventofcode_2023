import re
from typing import Optional, Self


class Symbol:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: Self) -> bool:
        if self.x != other.x or self.y != other.y:
            return False
        return True


class Number:
    def __init__(self, value: int, x_start: int, x_end: int, y: int) -> None:
        self.value = value
        self.x_start = x_start
        self.x_end = x_end
        self.y = y

    def __eq__(self, other: Self) -> bool:
        if (self.value != other.value or self.x_start != other.x_start or
                self.x_end != other.x_end or self.y != other.y):
            return False
        return True

    def is_touching(self, symbol: Symbol) -> bool:
        if abs(self.y - symbol.y) > 1:
            return False
        if self.x_start - 1 <= symbol.x <= self.x_end + 1:
            return True
        return False


def get_numbers(line: str, line_idx: int) -> list[Number]:
    numbers: list[Number] = []
    matches = re.finditer(r"\d+", line)
    for match in matches:
        s, e = match.start(), match.end()
        numbers.append(Number(int(line[s:e]), s, e-1, line_idx))
    return numbers


def get_symbols(line: str, line_idx: int) -> list[Symbol]:
    symbols: list[Symbol] = []
    matches = re.finditer(r"[^\.0-9]", line)
    for match in matches:
        symbols.append(Symbol(match.start(), line_idx))
    return symbols


def gear_ratios(input_string: str) -> tuple[int, int]:
    row_numbers = []
    symbols = []
    for i, line in enumerate(input_string.splitlines()):
        row_numbers.append(get_numbers(line, i))
        symbols.extend(get_symbols(line, i))

    max_y = len(row_numbers) - 1
    sum_ = 0
    sum_gears = 0
    for s in symbols:
        touches = []
        for i in range(min(0, s.y - 1), max(max_y, s.y + 1) + 1):
            for number in row_numbers[i]:
                if number.is_touching(s):
                    sum_ += number.value
                    touches.append(number.value)
        if len(touches) == 2:
            sum_gears += touches[0] * touches[1]

    return sum_, sum_gears


if __name__ == '__main__':
    with open("my_input", "r") as f:
        my_input = f.read()

    print(gear_ratios(my_input))
