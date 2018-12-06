#!/usr/local/bin/python3

"""
--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
"""

import math

def d( x1, y1, x2, y2 ):
    return abs( x1 - x2 ) + abs( y1 - y2 )

DATA = open("06.data","r")

#DATA = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]

points = [list(map(int, i.split(", ") )) for i in DATA]

(maxx, maxy, minx, miny) = (0,0,9**9,9**9)

for point in points:
    minx = min(minx, point[0])
    miny = min(miny, point[1])
    maxx = max(maxx, point[0])
    maxy = max(maxy, point[1])

owned = {}
for x in range(minx - 1, maxx + 2):
    for y in range(miny - 1, maxy + 2):
        mindist = math.inf
        for i in range(len(points)):
            dist = d(x, y, points[i][0], points[i][1])
            if dist < mindist:
                mindist = dist
                owned[(x,y)] = i
            elif dist == mindist:
                owned[(x,y)] = '*'

area = {}
for i in range(len(points)):
    area[i] = 0
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 1):
            if ( owned[(x,y)] == i ):
                if x == maxx or x == minx or y == miny or y == maxy:
                    area[i] = maxx * maxy
                    break
                area[i] += 1
        else:
            continue
        break

maxarea = 0
for i in range(len(points)):
    if area[i] == maxx * maxy:
        continue
    maxarea = max(area[i], maxarea)

print(maxarea)
