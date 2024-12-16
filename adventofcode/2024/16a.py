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

    queue = [(start, direction, "", 0)]
    lowest_cost = {(start, direction): 0} 
    while True:
        (pos, direction, path, cost) = queue.pop(0)
        if pos == end:
            return cost

        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos not in walls:
            if (new_pos,direction) not in lowest_cost or lowest_cost[(new_pos, direction)] > cost + 1:
                queue.append((new_pos, direction, path + "F", cost + 1))
                lowest_cost[(new_pos, direction)] = cost + 1

        if not path or path[-1] == "F":
            new_dir = turn_left(direction)
            if (pos, new_dir) not in lowest_cost or lowest_cost[(pos, new_dir)] > cost + 1000:
                queue.append((pos, new_dir, path + "L", cost + 1000))
                lowest_cost[(pos, new_dir)] = cost + 1000
            new_dir = turn_right(direction)
            if (pos, new_dir) not in lowest_cost or lowest_cost[(pos, new_dir)] > cost + 1000:
                queue.append((pos, new_dir, path + "R", cost + 1000))
                lowest_cost[(pos, new_dir)] = cost + 1000
        
        queue = sorted(queue, key=lambda e: e[3])
         


if __name__ == "__main__":
    walls, start, end = load_data("16.data")

    direction = (0,1)
    print(shortest_path(walls, start, end, direction))
