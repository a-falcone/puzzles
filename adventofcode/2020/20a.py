#!/usr/bin/env pypy3

"""
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
"""

import math

class Tile:
    def __init__(self, name):
        self._name = name
        self._data = []

    def __str__(self):
        s = f"Tile {self._name}:\n"
        s += "\n".join( self._data )
        return s

    def name(self):
        return self._name

    def add(self, line):
        self._data.append(line)

    def top(self):
        return self._data[0]

    def bottom(self):
        return self._data[-1]

    def left(self):
        return "".join([line[0] for line in self._data])

    def right(self):
        return "".join([line[-1] for line in self._data])

    def rotate(self):
        d = []
        size = len(self._data)
        for i in range(size):
            d.append("".join([line[size - i - 1] for line in self._data]))
        self._data = d
    
    def flip(self):
        d = []
        for line in self._data:
            d.append( line[::-1] )
        self._data = d

def solve(size, partial, tiles, edges):
    if len(partial) == size * size:
        return partial
    if not partial:
        #list is empty. try every tile in all 4 rotations
        for t in tiles:
            s = solve(size, [t], tiles, edges)
            if s:
                return s
            for i in range(3):
                tiles[t].rotate()
                s = solve(size, [t], tiles, edges)
                if s:
                    return s

    else:
        #list is not empty. find out where next tile goes. assemble list of candidates for next tile
        location = len(partial)
        candidates = set()
        if location >= size:
            #not first row. check above
            candidates.update(edges[tiles[partial[location - size]].bottom()])
        if location % size != 0:
            #not first column. check left
            candidates.update(edges[tiles[partial[location - 1]].right()])
        candidates.difference_update(partial)

        for candidate in candidates:
            for i in range(2):
                tiles[candidate].flip()
                for j in range(4):
                    tiles[candidate].rotate()
                    if location >= size:
                        if tiles[candidate].top() != tiles[partial[location - size]].bottom():
                            continue
                    if location % size != 0:
                        if tiles[candidate].left() != tiles[partial[location - 1]].right():
                            continue

                    partial.append(candidate)
                    s = solve( size, partial, tiles, edges )
                    if s:
                        return s

        partial.pop()
    return []

data = []

with open("20.data", "r") as f:
    for line in f:
        data.append(line.strip())

#data = [ 'Tile 2311:', '..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###', '', 'Tile 1951:', '#.##...##.', '#.####...#', '.....#..##', '#...######', '.##.#....#', '.###.#####', '###.##.##.', '.###....#.', '..#.#..#.#', '#...##.#..', '', 'Tile 1171:', '####...##.', '#..##.#..#', '##.#..#.#.', '.###.####.', '..###.####', '.##....##.', '.#...####.', '#.##.####.', '####..#...', '.....##...', '', 'Tile 1427:', '###.##.#..', '.#..#.##..', '.#.##.#..#', '#.#.#.##.#', '....#...##', '...##..##.', '...#.#####', '.#.####.#.', '..#..###.#', '..##.#..#.', '', 'Tile 1489:', '##.#.#....', '..##...#..', '.##..##...', '..#...#...', '#####...#.', '#..#.#.#.#', '...#.#.#..', '##.#...##.', '..##.##.##', '###.##.#..', '', 'Tile 2473:', '#....####.', '#..#.##...', '#.##..#...', '######.#.#', '.#...#.#.#', '.#########', '.###.#..#.', '########.#', '##...##.#.', '..###.#.#.', '', 'Tile 2971:', '..#.#....#', '#...###...', '#.#.###...', '##.##..#..', '.#####..##', '.#..####.#', '#..#.#..#.', '..####.###', '..#.#.###.', '...#.#.#.#', '', 'Tile 2729:', '...#.#.#.#', '####.#....', '..#.#.....', '....#..#.#', '.##..##.#.', '.#.####...', '####.#.#..', '##.####...', '##..#.##..', '#.##...##.', '', 'Tile 3079:', '#.#.#####.', '.#..######', '..#.......', '######....', '####.#..#.', '.#...#.##.', '#.#####.##', '..#.###...', '..#.......', '..#.###...' ]

tilename = ""
tiles = {}
for line in data:
    if line == "":
        continue
    line = line.strip()
    if line.startswith( "Tile" ):
        tilename = int(line.split(" ")[1].split(":")[0])
        tiles[tilename] = Tile(tilename)
    else:
        tiles[tilename].add(line)

edges = {}

for tilename in tiles:
    tile = tiles[tilename]
    for edge in tile.top(), tile.bottom(), tile.left(), tile.right():
        for final in edge, edge[::-1]:
            if final in edges:
                edges[final].append(tilename)
            else:
                edges[final] = [tilename]

size = int(math.sqrt(len(tiles)))

solution = solve(size, [], tiles, edges)

print(solution[0] * solution[size - 1] * solution[-1] * solution[size * (size - 1)])
