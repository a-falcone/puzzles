#!/usr/bin/env python3

"""
--- Day 16: Reindeer Maze ---
It's time again for the Reindeer Olympics! This year, the big event is the Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a total of 36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
In this maze, the best paths cost 11048 points; following one such path would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could possibly get?

--- Part Two ---
Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is whether the tile is on one of the best paths through the maze. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of any best path through the maze, including the S and E tiles.

In the first example, there are 45 tiles (marked O) that are part of at least one of the various best paths through the maze:

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############
In the second example, there are 64 tiles that are part of at least one of the best paths:

#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################
Analyze your map further. How many tiles are part of at least one of the best paths through the maze?
"""

def load_data(filename: str) -> list:
    walls = set()
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            line = line.rstrip()
            for x, c in enumerate(line):
                if c == "#":
                    walls.add((y,x))
                elif c == "S":
                    start = (y,x)
                elif c == "E":
                    end = (y,x)
    return walls, start, end

def turn_left(d):
    return (-d[1], d[0])

def turn_right(d):
    return (d[1], -d[0])

def cost(path):
    total = 0
    for c in path:
        if c == "F":
            total += 1
        else:
            total += 1000
    return total

def shortest_path(walls, start, end, direction):
    answers = set()
    queue = [(start, direction, set([start]), 0)]
    lowest_cost = {(start, direction): (0, set([start]))} 
    best = 9**9
    while True:
        (pos, direction, path, cost) = queue.pop(0)
        if (pos, direction) in lowest_cost and lowest_cost[(pos, direction)][0] == cost:
            path = path | lowest_cost[(pos, direction)][1]

        if pos == end:
            best = cost
            answers = answers | lowest_cost[(pos,direction)][1]
            continue

        if cost > best:
            return answers

        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos not in walls:
            if (new_pos, direction) not in lowest_cost:
                lowest_cost[(new_pos, direction)] = (cost + 1, path | set([new_pos]))
                queue.append((new_pos, direction, path | set([new_pos]), cost + 1))
            else:
                lc, lp = lowest_cost[(new_pos, direction)]
                if cost + 1 == lc:
                    lowest_cost[(new_pos, direction)] = (lc, lp | path)
                elif cost + 1 < lc:
                    queue.append((new_pos, direction, path | set([new_pos]), cost + 1))
                    lowest_cost[(new_pos, direction)] = (cost + 1, path)

        for new_dir in (turn_left(direction), turn_right(direction)):
            if (pos, new_dir) not in lowest_cost:
                lowest_cost[(pos, new_dir)] = (cost + 1000, path)
                queue.append((pos, new_dir, path, cost + 1000))
            else:
                lc, lp = lowest_cost[(pos, new_dir)]
                if cost + 1000 == lc:
                    lowest_cost[(pos, new_dir)] = (lc, lp | path)
                elif cost + 1000 < lc:
                    queue.append((pos, new_dir, path, cost + 1000))
                    lowest_cost[(pos, new_dir)] = (cost + 1000, path)

        
        queue = sorted(queue, key=lambda e: e[3])
         
if __name__ == "__main__":
    walls, start, end = load_data("16.data")

    direction = (0,1)
    print(len(shortest_path(walls, start, end, direction)))
