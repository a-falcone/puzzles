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

--- Part Two ---
The Elves were right to be concerned; the planned lagoon would be much too small.

After a few minutes, someone realizes what happened; someone swapped the color and instruction parameters when producing the dig plan. They don't have time to fix the bug; one of them asks if you can extract the correct instructions from the hexadecimal codes.

Each hexadecimal code is six hexadecimal digits long. The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.

So, in the above example, the hexadecimal codes can be converted into the true instructions:

#70c710 = R 461937
#0dc571 = D 56407
#5713f0 = R 356671
#d2c081 = D 863240
#59c680 = R 367720
#411b91 = D 266681
#8ceee2 = L 577262
#caa173 = U 829975
#1b58a2 = L 112010
#caa171 = D 829975
#7807d2 = L 491645
#a77fa3 = U 686074
#015232 = L 5411
#7a21e3 = U 500254
Digging out this loop and its interior produces a lagoon that can hold an impressive 952408144115 cubic meters of lava.

Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?
"""

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            instruction = line.rstrip().split()[2]
            l = instruction[2:7]
            d = instruction[7]
            data.append((int(l,16),int(d)))
    return data

def find_points(instructions: list) -> set:
    y,x = 0,0
    points = set()

    for l,d in instructions:
        if d == 0:
            yd, xd = 0, l
        elif d == 1:
            yd, xd = l, 0
        elif d == 2:
            yd, xd = 0, -l
        elif d == 3:
            yd, xd = -l, 0
        x += xd
        y += yd
        points.add((y,x))

    return sorted(list(points))

if __name__ == "__main__":
    instructions = load_data("18.data")
    
    points = sorted(find_points(instructions))
    segments = set()

    lava = 0
    lasty = points[0][0]

    for i in range(0, len(points), 2):
        p0, p1 = points[i], points[i+1]
        y = p0[0]
        x0, x1 = p0[1], p1[1]
        for segment in segments:
            lava += (segment[1] - segment[0] + 1) * (y - lasty)

        affected = []
        for segment in segments:
            if x0 in segment or x1 in segment or segment[0] < x0 < segment[1] or segment[0] < x1 < segment[1]:
                affected.append(segment)

        affected.sort()
        if len(affected) == 0:
            segments.add((x0,x1))
            lava += x1 - x0 + 1
        elif len(affected) == 1:
            segment = affected[0]
            segments.remove(segment)
            if x0 == segment[0] and x1 == segment[1]:
                pass
            elif segment[0] < x0 < x1 < segment[1]:
                segments.add((segment[0],x0))
                segments.add((x1,segment[1]))
            elif x0 == segment[0]:
                segments.add((x1,segment[1]))
            elif segment[1] == x1:
                segments.add((segment[0],x0))
            elif x1 == segment[0]:
                lava += segment[0] - x0 
                segments.add((x0, segment[1]))
            elif segment[1] == x0:
                lava += x1 - segment[1]
                segments.add((segment[0], x1))
        elif len(affected) == 2:
            s0 = affected[0]
            s1 = affected[1]
            segments.remove(s0)
            segments.remove(s1)
            segments.add((s0[0],s1[1]))
            lava += x1 - x0 - 1

        lasty = y

    print(lava)
