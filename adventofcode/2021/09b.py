#!/usr/bin/env python3

"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""

def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.strip())
    return data

def is_low(f, x, y):
    v = f[y][x]
    if x > 0 and f[y][x-1] <= v:
        return False
    if x < len(f[y]) - 1 and f[y][x+1] <= v:
        return False
    if y > 0 and f[y-1][x] <= v:
        return False
    if y < len(f) - 1 and f[y+1][x] <= v:
        return False
    return True

def size(f, x, y):
    pool = set([(x,y)])
    markpool(pool, f, x, y)
    return len(pool)

def markpool(p, f, x, y):
    if x > 0 and (x-1,y) not in p and f[y][x-1] != 9:
        p.add((x-1,y))
        markpool(p, f, x-1, y)
    if x < len(f[y]) - 1 and (x+1,y) not in p and f[y][x+1] != 9:
        p.add((x+1,y))
        markpool(p, f, x+1, y)
    if y > 0 and (x,y-1) not in p and f[y-1][x] != 9:
        p.add((x,y-1))
        markpool(p, f, x, y-1)
    if y < len(f) - 1 and (x,y+1) not in p and f[y+1][x] != 9:
        p.add((x,y+1))
        markpool(p, f, x, y+1)

if __name__ == "__main__":
    data = load_data("09.data")
    field = []
    for line in data:
        field.append([int(i) for i in list(line)])
    basins = []
    for y in range(len(field)):
        for x in range(len(field[y])):
            if is_low(field, x, y):
                basins.append(size(field, x, y))
    basins = sorted(basins)
    print(basins[-1] * basins[-2] * basins[-3])
