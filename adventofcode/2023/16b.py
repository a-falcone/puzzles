#!/usr/bin/env python3

"""
--- Day 16: The Floor Will Be Lava ---
With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.

Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.
If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.
Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?

--- Part Two ---
As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\....
|v-v\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\
.v//.|.v..
Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..
Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
"""

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

def load_data(filename: str) -> list:
    mirrors = dict()
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.rstrip()):
                if c != ".":
                    mirrors[(y,x)] = c
    return mirrors, y+1, x+1

def step(beam: tuple, mirrors: dict, rows: int, cols: int) -> list:
    y,x = beam[0]
    direction = beam[1]
    y += direction[0]
    x += direction[1]
    if y < 0 or y >= rows or x < 0 or x >= cols:
        return []

    if (y,x) not in mirrors:
        return [((y,x),direction)]

    mirror = mirrors[(y,x)]

    if mirror == "-":
        if direction == LEFT or direction == RIGHT:
            return [((y,x),direction)]
        elif direction == UP or direction == DOWN:
            return [((y,x),LEFT),
                    ((y,x),RIGHT)]
    elif mirror == "|":
        if direction == UP or direction == DOWN:
            return [((y,x),direction)]
        elif direction == LEFT or direction == RIGHT:
            return [((y,x),UP),
                    ((y,x),DOWN)]
    elif mirror == "/":
        if direction == UP:
            return [((y,x),RIGHT)]
        elif direction == DOWN:
            return [((y,x),LEFT)]
        elif direction == RIGHT:
            return [((y,x),UP)]
        elif direction == LEFT:
            return [((y,x),DOWN)]
    elif mirror == "\\":
        if direction == UP:
            return [((y,x),LEFT)]
        elif direction == DOWN:
            return [((y,x),RIGHT)]
        elif direction == RIGHT:
            return [((y,x),DOWN)]
        elif direction == LEFT:
            return [((y,x),UP)]

if __name__ == "__main__":
    mirrors, rows, cols = load_data("16.data")

    maxen = 0
    for y in range(rows):
        active = set([((y,-1),(0,1))])
        energized = set()
        seen = set()

        while len(active) > 0:
            newbeams = set()
            for beam in active:
                beams = step(beam, mirrors, rows, cols)
                for b in beams:
                    energized.add(b[0])
                    if b not in seen:
                        newbeams.add(b)
                        seen.add(b)

            active = newbeams
        maxen = max(len(energized), maxen)

        active = set([((y,cols),(0,-1))])
        energized = set()
        seen = set()

        while len(active) > 0:
            newbeams = set()
            for beam in active:
                beams = step(beam, mirrors, rows, cols)
                for b in beams:
                    energized.add(b[0])
                    if b not in seen:
                        newbeams.add(b)
                        seen.add(b)

            active = newbeams
        maxen = max(len(energized), maxen)

    for x in range(cols):
        active = set([((-1,x),(1,0))])
        energized = set()
        seen = set()

        while len(active) > 0:
            newbeams = set()
            for beam in active:
                beams = step(beam, mirrors, rows, cols)
                for b in beams:
                    energized.add(b[0])
                    if b not in seen:
                        newbeams.add(b)
                        seen.add(b)

            active = newbeams
        maxen = max(len(energized), maxen)

        active = set([((rows,x),(-1,0))])
        energized = set()
        seen = set()

        while len(active) > 0:
            newbeams = set()
            for beam in active:
                beams = step(beam, mirrors, rows, cols)
                for b in beams:
                    energized.add(b[0])
                    if b not in seen:
                        newbeams.add(b)
                        seen.add(b)

            active = newbeams
        maxen = max(len(energized), maxen)

    print(maxen)
