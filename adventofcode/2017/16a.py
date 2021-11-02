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

def spin( l, d ):
    return l[len(l)-d:] + l[:len(l)-d]

def exchange( l, a, b ):
    a, b = int(a), int(b)
    c, d = min(a,b), max(a,b)
    return l[:c] + [l[d]] + l[c+1:d] + [l[c]] + l[d+1:]

def partner( l, a, b ):
    la, lb = l.index(a), l.index(b)
    c, d = min(la,lb), max(la,lb)
    return l[:c] + [l[d]] + l[c+1:d] + [l[c]] + l[d+1:]

data = []
with open( "data/16.data", "r" ) as f:
    line = f.read().strip()
    data = line.split(",")

s = list("abcdefghijklmnop")

#data = ["s1", "x3/4", "pe/b"]
#s = list("abcde")

for instruction in data:
    if instruction[0] == "s":
        s = spin( s, int(instruction[1:]) )
    elif instruction[0] == "x":
        s = exchange( s, *instruction[1:].split("/") )
    else:
        s = partner( s, *instruction[1:].split("/") )

print( "".join(s) )
