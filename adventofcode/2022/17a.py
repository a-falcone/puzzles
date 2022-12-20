#!/usr/bin/env pypy3

"""
--- Day 17: Pyroclastic Flow ---
Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+
The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+
To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
"""

def load_data(filename: str) -> list:
    with open(filename, "r") as f:
        line = f.read()
        return line.rstrip()

def printboard(board: set, maxheight: int, workingpiece: list, width: int):
    print(f"maxheight = {maxheight}")
    for y in range(maxheight + 6, 0, -1):
        print("|", end ="")
        for x in range(width):
            if (x,y) in board:
                print("#", end="")
            elif [x,y] in workingpiece:
                print("o", end="")
            else:
                print(".", end="")
        print("|")
    print(f"+{'-'*width}+")

def shiftpiece(direction: str, workingpiece: list) -> list:
    offset = 1
    if direction == "<":
        offset = -1
    shiftedpiece = []
    for c in workingpiece:
        shiftedpiece.append([c[0] + offset, c[1]])
    return shiftedpiece

def droppiece(workingpiece: list) -> list:
    shiftedpiece = []
    for c in workingpiece:
        shiftedpiece.append([c[0], c[1] - 1])
    return shiftedpiece

if __name__ == "__main__":
    data = load_data("17.data")

    WIDTH = 7
    LASTPIECE = 2022
    pieces = [
                [[2,0], [3,0], [4,0], [5,0]],
                [[3,0], [2,1], [3,1], [4,1], [3,2]],
                [[2,0], [3,0], [4,0], [4,1], [4,2]],
                [[2,0], [2,1], [2,2], [2,3]],
                [[2,0], [3,0], [2,1], [3,1]]
             ]

    maxheight, piecenumber, inputpos, board = 0, 0, 0, set()

    while piecenumber < LASTPIECE:
        workingpiece = [c[:] for c in pieces[piecenumber % 5]]

        for c in workingpiece:
            c[1] += maxheight + 4

        locked = False
        while not locked:
            direction = data[inputpos]
            inputpos = (inputpos + 1) % len(data)

            newloc = shiftpiece(direction, workingpiece)
            for c in newloc:
                if tuple(c) in board or c[0] < 0 or c[0] >= WIDTH:
                    break
            else:
                workingpiece = newloc

            newloc = droppiece(workingpiece) 
            for c in newloc:
                if tuple(c) in board or c[1] <= 0:
                    locked = True
                    for d in workingpiece:
                        board.add(tuple(d))
                        maxheight = max(maxheight, d[1])
                    break
            else:
                workingpiece = newloc

        piecenumber += 1
    print(maxheight)
