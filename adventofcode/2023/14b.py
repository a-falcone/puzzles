#!/usr/bin/env python3

"""
--- Day 14: Parabolic Reflector Dish ---
You reach the place where all of the mirrors were pointing: a massive parabolic reflector dish attached to the side of another large mountain.

The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.

This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.

Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.

In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
"""

def load_data(filename: str) -> list:
    rocks, pillars = [], []
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.rstrip()):
                if c == "O":
                    rocks.append((y,x))
                elif c == "#":
                    pillars.append((y,x))
    return tuple(rocks), set(pillars), y+1, x+1

def display(rocks: tuple, pillars: set, rows: int, cols: int) -> None:
    rocks = set(rocks)
    for y in range(rows):
        for x in range(cols):
            if (y,x) in rocks:
                if (y,x) in pillars:
                    print(f"Rock and pillar in {(y,x)}")
                    exit()
                c = "O"
            elif (y,x) in pillars:
                c = "#"
            else:
                c = "."
            print(c, end="")
        print()

def northstress(rocks: tuple, rows: int) -> int:
    total = 0
    for rock in rocks:
        total += rows - rock[0]
    return total

def rollnorth(rocks: tuple, pillars: set, rows: int) -> tuple:
    newrocks = set()
    for rock in sorted(rocks, key=lambda r: r[0]):
        y, x = rock
        while y > 0:
            if (y-1,x) not in newrocks and (y-1,x) not in pillars:
                y -= 1
            else:
                break
        newrocks.add((y,x))
    return tuple(newrocks)

def rollsouth(rocks: tuple, pillars: set, rows: int) -> tuple:
    newrocks = set()
    for rock in sorted(rocks, reverse=True, key=lambda r: r[0]):
        y, x = rock
        while y < rows - 1:
            if (y+1,x) not in newrocks and (y+1,x) not in pillars:
                y += 1
            else:
                break
        newrocks.add((y,x))
    return tuple(newrocks)

def rollwest(rocks: tuple, pillars: set, cols: int) -> tuple:
    newrocks = set()
    for rock in sorted(rocks, key=lambda r: r[1]):
        y, x = rock
        while x > 0:
            if (y,x-1) not in newrocks and (y,x-1) not in pillars:
                x -= 1
            else:
                break
        newrocks.add((y,x))
    return tuple(newrocks)

def rolleast(rocks: tuple, pillars: set, cols: int) -> tuple:
    newrocks = set()
    for rock in sorted(rocks, reverse=True, key=lambda r: r[1]):
        y, x = rock
        while x < cols - 1:
            if (y,x+1) not in newrocks and (y,x+1) not in pillars:
                x += 1
            else:
                break
        newrocks.add((y,x))
    return tuple(newrocks)

def cycle(rocks: tuple, pillars: set, rows: int, cols: int) -> tuple:
    rocks = rollnorth(rocks, pillars, rows)
    rocks = rollwest(rocks, pillars, cols)
    rocks = rollsouth(rocks, pillars, rows)
    rocks = rolleast(rocks, pillars, cols)
    return rocks

if __name__ == "__main__":
    times = 1_000_000_000
    rocks, pillars, rows, cols = load_data("14.data")

    seen = {rocks:0}

    rocks = cycle(rocks, pillars, rows, cols)
    i = 1
    while rocks not in seen and i < times:
        seen[rocks] = i
        rocks = cycle(rocks, pillars, rows, cols)
        i += 1
   
    if times == i:
        print(northstress(rocks, rows))
    else:
        period = i - seen[rocks]
        residual = (times - seen[rocks]) % period
        target = seen[rocks] + residual
        for cycle, index in seen.items():
            if index == target:
                print(northstress(cycle, rows))
