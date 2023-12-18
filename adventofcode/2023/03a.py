#!/usr/bin/env python3

"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

import re

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.rstrip())
    return data

def symbol_around(loc: tuple, number: int, symbols: dict) -> bool:
    for y in (loc[0] - 1, loc[0] + 1):
        for x in range(loc[1] - 1, loc[1] + len(str(number)) + 1):
            if (y,x) in symbols:
                return True
    
    for x in (loc[1] - 1, loc[1] + len(str(number))):
        if (loc[0], x) in symbols:
            return True

    return False

if __name__ == "__main__":
    data = load_data("03.data")

    symbols = {}
    numbers = {}

    for y, line in enumerate(data):
        for match in re.finditer("\d+", line):
            numbers[(y,match.start())] = int(match.group())
        
        for x, c in enumerate(line):
            if c != '.' and not c.isdigit():
                symbols[(y,x)] = c
                
    total = 0
    for loc, number in numbers.items():
        if symbol_around(loc, number, symbols):
            total += number

    print(total)
