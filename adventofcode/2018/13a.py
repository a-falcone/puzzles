#!/usr/local/bin/python3

"""
--- Day 13: Mine Cart Madness ---
A crop of this size requires significant logistics to transport produce, soil, fertilizer, and so on. The Elves are very busy pushing things around in carts on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for another 1000 years, the Elves seem to be making this up as they go along. They haven't even figured out how to avoid collisions yet.

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (| and -), curves (/ and \), and intersections (+). Curves connect exactly two perpendicular pieces of track; for example, this is a closed loop:

/----\
|    |
|    |
\----/
Intersections occur when two perpendicular paths cross. At an intersection, a cart is capable of turning left, turning right, or continuing straight. Here are two loops connected by two intersections:

/-----\
|     |
|  /--+--\
|  |  |  |
\--+--/  |
   |     |
   \-----/
Several carts are also on the tracks. Carts always face either up (^), down (v), left (<), or right (>). (On your initial map, the track under each cart is a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it turns left the first time, goes straight the second time, turns right the third time, and then repeats those directions starting again with left the fourth time, straight the fifth time, and so on. This process is independent of the particular intersection at which the cart has arrived - that is, the cart has no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a time. They do this based on their current location: carts on the top row move first (acting from left to right), then carts on the second row move (again from left to right), then carts on the third row, and so on. Once each cart has moved one step, the process repeats; each of these loops is called a tick.

For example, suppose there are two carts on a straight track:

|  |  |  |  |
v  |  |  |  |
|  v  v  |  |
|  |  |  v  X
|  |  ^  ^  |
^  ^  |  |  |
|  |  |  |  |
First, the top cart moves. It is facing down (v), so it moves down one square. Second, the bottom cart moves. It is facing up (^), so it moves up one square. Because all carts have moved, the first tick ends. Then, the process repeats, starting with the first cart. The first cart moves down, then the second cart moves up - right into the first cart, colliding with it! (The location of the crash is marked with an X.) This ends the second and last tick.

Here is a longer example:

/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/-->\
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/

/---v
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/

/---\
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/

/---\
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/

/---\
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/

/---\
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/

/---\
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/

/---\
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/

/---\
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/

/---\
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/

/---\
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/
After following their respective paths for a while, the carts eventually crash. To help prevent crashes, you'd like to know the location of the first crash. Locations are given in X,Y coordinates, where the furthest left column is X=0 and the furthest top row is Y=0:

           111
 0123456789012
0/---\
1|   |  /----\
2| /-+--+-\  |
3| | |  X |  |
4\-+-/  \-+--/
5  \------/
In this example, the location of the first crash is 7,3.

"""

DATA=open("13.data","r")
#DATA=[r"/->-\ ", r"|   |  /----\ ", r"| /-+--+-\  | ", r"| | |  | v  | ", r"\-+-/  \-+--/ ", r"  \------/ "]
#DATA=["/>\\","\\-+\\","  \\/"]

tracks = {}
carts = {}
turns = {">": "^>v", "^": "<^>", "<": "v<^", "v": ">v<"}

def printit():
    for y in range(6):
        for x in range(200):
            if (x,y) in tracks:
                if (x,y) in carts:
                    print(carts[(x,y)][0], end="")
                else:
                    print(tracks[(x,y)], end="")
        print()


x = 0
y = 0
for line in DATA:
    line = line.rstrip()
    for c in line:
        if c == ">" or c == "<":
            tracks[(x,y)] = "-"
            carts[(x,y)] = (c, 0)
        elif c == "^" or c == "v":
            tracks[(x,y)] = "|"
            carts[(x,y)] = (c, 0)
        else:
            tracks[(x,y)] = c
        x += 1
    y += 1
    x = 0

def takeSecond(elem):
    return elem[1]

r = 0
while(True):
    curloc = list(carts.keys())
    newcarts = {}
    r += 1
    for c in sorted(carts.keys(), key=takeSecond):
        direction = carts[c][0]
        turnno = carts[c][1]
        delta = ()
        if direction == ">":
            delta = (1,0)
        elif direction == "^":
            delta = (0,-1)
        elif direction == "<":
            delta = (-1,0)
        elif direction == "v":
            delta = (0,1)
        else:
            quit("1what happened?")
        newloc = (c[0] + delta[0], c[1] + delta[1])
        if newloc in curloc:
            print(newloc, r)
            quit()
        curloc.append(newloc)
        curloc.remove(c)
        if tracks[newloc] == "\\":
            if direction == "<":
                newcarts[newloc] = ("^", turnno)
            elif direction == "v":
                newcarts[newloc] = (">", turnno)
            elif direction == ">":
                newcarts[newloc] = ("v", turnno)
            elif direction == "^":
                newcarts[newloc] = ("<", turnno)
            else:
                quit("2what happened?")
        elif tracks[newloc] == "/":
            if direction == "<":
                newcarts[newloc] = ("v", turnno)
            elif direction == "v":
                newcarts[newloc] = ("<", turnno)
            elif direction == ">":
                newcarts[newloc] = ("^", turnno)
            elif direction == "^":
                newcarts[newloc] = (">", turnno)
            else:
                quit("3what happened?")
        elif tracks[newloc] == "+":
            newcarts[newloc] = (turns[direction][turnno], (turnno + 1) % 3)
        else:
            newcarts[newloc] = (direction, carts[c][1])
            
    carts = newcarts
