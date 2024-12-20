#!/usr/bin/env python3

"""
--- Day 20: Race Condition ---
The Historians are quite pixelated again. This time, a massive, black building looms over you - you're right outside the CPU!

While The Historians get to work, a nearby program sees that you're idle and challenges you to a race. Apparently, you've arrived just in time for the frequently-held race condition festival!

The race takes place on a particularly long and twisting code path; programs compete to see who can finish in the fewest picoseconds. The winner even gets their very own mutex!

They hand you a map of the racetrack (your puzzle input). For example:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
The map consists of track (.) - including the start (S) and end (E) positions (both of which also count as track) - and walls (#).

When a program runs through the racetrack, it starts at the start position. Then, it is allowed to move up, down, left, or right; each such move takes 1 picosecond. The goal is to reach the end position as quickly as possible. In this example racetrack, the fastest time is 84 picoseconds.

Because there is only a single path from the start to the end and the programs all go the same speed, the races used to be pretty boring. To make things more interesting, they introduced a new rule to the races: programs are allowed to cheat.

The rules for cheating are very strict. Exactly once during a race, a program may disable collision for up to 2 picoseconds. This allows the program to pass through walls as if they were regular track. At the end of the cheat, the program must be back on normal track again; otherwise, it will receive a segmentation fault and get disqualified.

So, a program could complete the course in 72 picoseconds (saving 12 picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...12....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Or, a program could complete the course in 64 picoseconds (saving 20 picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...12..#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
This cheat saves 38 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.####1##.###
#...###.2.#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
This cheat saves 64 picoseconds and takes the program directly to the end:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..21...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Each cheat has a distinct start position (the position where the cheat is activated, just before the first move that is allowed to go through walls) and end position; cheats are uniquely identified by their start position and end position.

In this example, the total number of cheats (grouped by the amount of time they save) are as follows:

There are 14 cheats that save 2 picoseconds.
There are 14 cheats that save 4 picoseconds.
There are 2 cheats that save 6 picoseconds.
There are 4 cheats that save 8 picoseconds.
There are 2 cheats that save 10 picoseconds.
There are 3 cheats that save 12 picoseconds.
There is one cheat that saves 20 picoseconds.
There is one cheat that saves 36 picoseconds.
There is one cheat that saves 38 picoseconds.
There is one cheat that saves 40 picoseconds.
There is one cheat that saves 64 picoseconds.
You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible, you'll need a list of the best cheats. How many cheats would save you at least 100 picoseconds?
"""

def load_data(filename: str) -> list:
    maxx, maxy = 0, 0
    walls = set()
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            line = line.rstrip()
            maxx = len(line)
            maxy = max(maxy, y)
            for x, c in enumerate(line):
                if c == 'S':
                    start = (y,x)
                elif c == 'E':
                    end = (y,x)
                elif c == '#':
                    walls.add((y,x))
    maxy += 1
    return walls, start, end, maxy, maxx

def inbounds(pos, maxx, maxy):
    return (0 <= pos[0] < maxy) and (0 <= pos[1] < maxx)

def solve_maze(walls, start, end, maxx, maxy):
    queue = [(start,)]
    while queue:
        path = queue.pop(0)
        pos = path[-1]
        if pos == end:
            return path
        for d in ((0,1), (0,-1), (1,0), (-1,0)):
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if newpos not in walls and newpos not in path:
                queue.append(path + (newpos,))

def saves(walls, costs, maxx, maxy):
    cheats = {}
    for pos in costs:
        for d in ((0,1), (0,-1), (1,0), (-1,0)):
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if newpos not in walls:
                continue
            end_cheat = (pos[0] + 2*d[0], pos[1] + 2*d[1])
            if inbounds(end_cheat, maxy, maxx) and end_cheat not in walls:
                savings = costs[end_cheat] - costs[pos] - 2
                if savings > 0:
                    cheats[(newpos, end_cheat)] = savings
    return cheats

if __name__ == "__main__":
    walls, start, end, maxy, maxx = load_data("20.data")

    baseline = solve_maze(walls, start, end, maxx, maxy)
    costs = {}
    for i, p in enumerate(baseline):
        costs[p] = i
    cheats = saves(walls, costs, maxx, maxy)
    total = 0
    for c in cheats:
        if cheats[c] >= 100:
            total += 1
    print(total)
