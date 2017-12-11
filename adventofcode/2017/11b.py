#!/usr/local/bin/python3

"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""

f = open("data/11.data", "r")
line = f.read()

def dist( p ):
    return int(abs(p[0]) + max(0, abs(p[1]) - abs(p[0]) / 2) )

pos=[0,0]
m=dist(pos)
for d in line.split(","):
    d = d.strip()
    if d == "n":
        pos[1] += 1
    elif d == "ne":
        pos[0] += 1
        pos[1] += .5
    elif d == "nw":
        pos[0] -= 1
        pos[1] += .5
    elif d == "s":
        pos[1] -= 1
    elif d == "se":
        pos[0] += 1
        pos[1] -= .5
    elif d == "sw":
        pos[0] -= 1
        pos[1] -= .5
    else:
        print( "unknown, >", d, "<")
    if dist(pos) > m:
        m = dist(pos)
 
print( m )
