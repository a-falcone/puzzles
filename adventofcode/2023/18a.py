#!/usr/bin/env python3

"""
--- Day 18: Lavaduct Lagoon ---
Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.

However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.

When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######
At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######
Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.

The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
"""

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            d, l, color = line.rstrip().split()
            l = int(l)
            color = color[2:8]
            data.append((d,l,color))
    return data

m = {
        "R": (0,1),
        "L": (0,-1),
        "U": (-1,0),
        "D": (1,0)
    }

def build_walls(data: list) -> tuple:
    maxx, minx, maxy, miny = 0, 0, 0, 0
    y,x = 0,0
    walls = {}
    for d, l, color in data:
        ydelta, xdelta = m[d]
        for _ in range(l):
            y += ydelta
            x += xdelta
            walls[(y,x)] = color
        miny = min(y,miny)
        maxy = max(y,maxy)
        minx = min(x,minx)
        maxx = max(x,maxx)
    return walls, miny, maxy, minx, maxx

def find_interior_point(walls: dict, miny: int, minx: int) -> tuple:
    y = miny
    while True:
        y += 1
        x = minx
        while True:
            if (y,x) in walls:
                if (y,x+1) not in walls:
                    return (y,x+1)
                break
            x += 1

def fill_interior(walls: dict, interior_point: tuple) -> dict:
    to_check = set([interior_point])
    interior = {interior_point: None}
    while to_check:
        y,x = to_check.pop()
        for dx,dy in (0,1), (0,-1), (1,0), (-1,0):
            p = (y+dy,x+dx)
            if p not in walls and p not in interior:
                interior[p] = None
                to_check.add(p)
    return interior

if __name__ == "__main__":
    data = load_data("18.data")

    walls, miny, maxy, minx, maxx = build_walls(data)

    interior_point = find_interior_point(walls, miny, minx)
    interior = fill_interior(walls, interior_point)

    print(len(walls) + len(interior))
