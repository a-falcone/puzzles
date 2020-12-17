#!/usr/bin/env pypy3

"""
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?
"""

def remove( f, x, y, z ):
    if z not in f:
        return
    if y not in f[z]:
        return
    if x in f[z][y]:
        f[z][y].pop(x)
    if not f[z][y]:
        f[z].pop(y)
    if not f[z]:
        f.pop(z)

def add( f, x, y, z ):
    if z not in f:
        f[z] = {}
    if y not in f[z]:
        f[z][y] = {}
    f[z][y][x] = True

def get( f, x, y, z ):
    if z not in f:
        return False
    if y not in f[z]:
        return False
    return f[z][y].get(x, False)

def neighbors( f, x, y, z ):
    n = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx == dy == dz == 0:
                    continue
                if get( f, x + dx, y + dy, z + dz ):
                    n += 1
    return n
                
def evolve( f ):
    cf = {}
    minz, maxz = min( f.keys() ), max( f.keys() )
    miny, maxy, minx, maxx = 0, 0, 0, 0
    for z in f:
        miny, maxy = min( miny, *f[z].keys() ), max( maxy, *f[z].keys() )
        for y in f[z]:
            minx, maxx = min( minx, *f[z][y].keys() ), max( maxx, *f[z][y].keys() )
    for z in range(minz - 1, maxz + 2):
        for y in range(miny - 1, maxy + 2):
            for x in range(minx - 1, maxx + 2):
                if get( f, x, y, z ):
                    n = neighbors( f, x, y, z )
                    if n == 2 or n == 3:
                        add( cf, x, y, z )
                else:
                    if neighbors( f, x, y, z ) == 3:
                        add( cf, x, y, z )
    return cf
                    

def count( f ):
    c = 0
    for z in f:
        for y in f[z]:
            for x in f[z][y]:
                if f[z][y][x]:
                    c += 1
    return c

data = []

with open("17.data", "r") as f:
    for line in f:
        data.append(line.strip())

f = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "#":
            add( f, x, y, 0 )

for i in range(6):
    f = evolve(f)

print(count(f))
