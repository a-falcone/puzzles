#!/usr/bin/env python3

"""
--- Day 15: Warehouse Woes ---
You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 4 = 104.

#######
#...O..
#......
The lanternfish would like to know the sum of all boxes' GPS coordinates after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of all boxes' GPS coordinates?

--- Part Two ---
The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is twice as wide! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
After appropriately resizing this map, the robot would push around these boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of 1 from the top edge of the map and 5 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........
In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?
"""

def load_data(filename: str) -> list:
    walls = set()
    boulders = set()
    instructions = ""
    y = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("#"):
                for x,c in enumerate(line):
                    if c == "@":
                        pos = (y, 2*x)
                    elif c == "#":
                        walls.add((y,2*x))
                        walls.add((y,2*x+1))
                    elif c == "O":
                        boulders.add((y,2*x))
                y += 1
            elif line:
                instructions += line

    return walls, boulders, instructions, pos

def above(pos):
    return (pos[0] - 1, pos[1])

def below (pos):
    return (pos[0] + 1, pos[1])

def rightof(pos):
    return (pos[0], pos[1] + 1)

def leftof(pos):
    return (pos[0], pos[1] - 1)

def move(walls, boulders, d, pos):
    newpos = (pos[0] + d[0], pos[1] + d[1])
    if newpos in walls:
        return boulders, pos

    if newpos not in boulders and leftof(newpos) not in boulders:
        return boulders, newpos

    newboulders = boulders.copy()
    if d == (0,1):
        i = 1
        target = newpos
        while target in boulders and target not in walls:
            newboulders.remove(target)
            newboulders.add(rightof(target))
            target = rightof(rightof(target))
        if target in walls:
            return boulders, pos
        else:
            return newboulders, newpos

    elif d == (0,-1):
        target = newpos
        while leftof(target) in boulders and leftof(target) not in walls:
            newboulders.remove(leftof(target))
            newboulders.add(leftof(leftof(target)))
            target = leftof(leftof(target))
        if target in walls:
            return boulders, pos
        else:
            return newboulders, newpos

    elif d == (1,0):
        moved = set()
        if newpos in boulders:
            moved.add(newpos)
            newboulders.add(below(newpos))
            newboulders.remove(newpos)
        else:
            moved.add(leftof(newpos))
            newboulders.add(leftof(below(newpos)))
            newboulders.remove(leftof(newpos))
        didmove = True
        while didmove:
            didmove = False
            newmoved = set()
            for b in moved:
                if below(b) in walls or below(rightof(b)) in walls:
                    return boulders, pos

                if below(b) in boulders:
                    newboulders.add(below(below(b)))
                    newmoved.add(below(b))
                    didmove = True
                if leftof(below(b)) in newboulders: 
                    newboulders.remove(leftof(below(b)))
                    newboulders.add(below(leftof(below(b))))
                    newmoved.add(leftof(below(b)))
                    didmove = True
                if rightof(below(b)) in newboulders: 
                    newboulders.remove(rightof(below(b)))
                    newboulders.add(below(rightof(below(b))))
                    newmoved.add(rightof(below(b)))
                    didmove = True
            moved = newmoved
        return newboulders, newpos

    elif d == (-1,0):
        moved = set()
        if newpos in boulders:
            moved.add(newpos)
            newboulders.add(above(newpos))
            newboulders.remove(newpos)
        else:
            moved.add(leftof(newpos))
            newboulders.add(above(leftof(newpos)))
            newboulders.remove(leftof(newpos))
        didmove = True
        while didmove:
            didmove = False
            newmoved = set()
            for b in moved:
                if above(b) in walls or above(rightof(b)) in walls:
                    return boulders, pos

                if above(b) in boulders:
                    newboulders.add(above(above(b)))
                    newmoved.add(above(b))
                    didmove = True
                if leftof(above(b)) in newboulders: 
                    newboulders.remove(leftof(above(b)))
                    newboulders.add(above(leftof(above(b))))
                    newmoved.add(leftof(above(b)))
                    didmove = True
                if rightof(above(b)) in newboulders: 
                    newboulders.remove(rightof(above(b)))
                    newboulders.add(above(rightof(above(b))))
                    newmoved.add(rightof(above(b)))
                    didmove = True
            moved = newmoved
        return newboulders, newpos

    return boulders, pos

if __name__ == "__main__":
    walls, boulders, instructions, pos = load_data("15.data")

    directions = {"^": (-1,0), "v": (1,0), "<": (0,-1), ">": (0,1)}
    for instruction in instructions:
        boulders, pos = move(walls, boulders, directions[instruction], pos)
    
    score = 0
    for b in boulders:
        score += 100*b[0] + b[1]
    print(score)
