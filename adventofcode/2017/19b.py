#!/usr/bin/env python3

def load_data(filename: str) -> list:
    data = {}
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            line = line.rstrip()
            for x, c in enumerate(line):
                if c != ' ':
                    data[(y,x)] = c
    return data

if __name__ == "__main__":
    data = load_data("19.data")

    for x in range(1000):
        if (0, x) in data:
            pos = (0, x)
            break

    count = 1
    d = (1,0)
    while True:
        c = data[pos]

        newpos = (pos[0] + d[0], pos[1] + d[1])

        if newpos in data:
            pos = newpos
            count += 1
            continue

        if d in ((1,0), (-1,0)):
            choices = ((0,1), (0,-1))
        else:
            choices = ((1,0), (-1,0))
        for d in choices:
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if newpos in data:
                pos = newpos
                count += 1
                break
        else:
            break

    print(count)

"""
--- Day 19: A Series of Tubes ---
Somehow, a network packet got lost and ended up here. It's trying to follow a routing diagram (your puzzle input), but it's confused about where to go.

Its starting point is just off the top of the diagram. Lines (drawn with |, -, and +) show the path it needs to take, starting by going down onto the only line connected to the top of the diagram. It needs to follow this path until it reaches the end (located somewhere within the diagram) and stop there.

Sometimes, the lines cross over each other; in these cases, it needs to continue going the same direction, and only turn left or right when there's no other option. In addition, someone has left letters on the line; these also don't change its direction, but it can use them to keep track of where it's been. For example:

     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 

Given this diagram, the packet needs to take the following path:

Starting at the only line touching the top of the diagram, it must go down, pass through A, and continue onward to the first +.
Travel right, up, and right, passing through B in the process.
Continue down (collecting C), right, and up (collecting D).
Finally, go all the way left through E and stopping at F.
Following the path to the end, the letters it sees on its path are ABCDEF.

The little packet looks up at you, hoping you can help it find the way. What letters will it see (in the order it would see them) if it follows the path? (The routing diagram is very wide; make sure you view it without line wrapping.)
"""
