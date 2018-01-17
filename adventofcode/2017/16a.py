#!/usr/local/bin/python3

"""
You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

  Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
  Exchange, written xA/B, makes the programs at positions A and B swap places.
  Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do the following dance:

  s1, a spin of size 1: eabcd.
  x3/4, swapping the last two programs: eabdc.
  pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?
"""

import re

def find( dancers, dancer1, dancer2 ):
    for i in range(len(dancers)):
        if dancers[i] == dancer1:
            pos1 = i
        if dancers[i] == dancer2:
            pos2 = i
    return pos1, pos2


data = ["s1,x3/4,pe/b"]
group = list( "abcde" )
data = open( "data/16.data", "r" )
group = list( "abcdefghijklmnop" )

for line in data:
    for move in line.split(","):
        if move[0] == "s":
            spin = int(re.findall("\d+", move)[0])
            tail = group[-1 * spin:]
            del(group[-1 * spin:])
            group[0:0] = tail
        elif move[0] == "x":
            pos1, pos2 = re.findall("\d+", move)
            group[int(pos1)], group[int(pos2)] = group[int(pos2)], group[int(pos1)]
        elif move[0] == "p":
            dancer1, dancer2 = move[1], move[3]
            pos1, pos2 = find(group, dancer1, dancer2)
            group[int(pos1)], group[int(pos2)] = group[int(pos2)], group[int(pos1)]

print( "".join(group) )
