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

def printtile( tile ):
    print( f"Tile {tile['name']}:" )
    for i in tile["body"]:
        print( i )

def fittiles( t1, t2 ):
    edges = {}
    edges['top'] = [ t1['body'][0], t2['body'][0] ]
    edges['bottom'] = [ t1['body'][-1], t2['body'][-1] ]
    edges['left'] = [ "".join([ i[0] for i in t1['body']]), "".join([ i[0] for i in t2['body']]) ]
    edges['right'] = [ "".join([ i[-1] for i in t1['body']]), "".join([ i[-1] for i in t2['body']]) ]
    for i in "top", "bottom", "left", "right":
        for j in "top", "bottom", "left", "right":
            if edges[i][0] == edges[j][1]:
                print( f"{t2['name']} is on {j} of {t1['name']}" )
            if edges[i][0] == edges[j][1][::-1]:
                print( f"{t2['name']} is on {j} of {t1['name']} reversed" )
            

data = []

with open("20.data", "r") as f:
    for line in f:
        data.append(line.strip())

#data = [ 'Tile 2311:', '..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###', '', 'Tile 1951:', '#.##...##.', '#.####...#', '.....#..##', '#...######', '.##.#....#', '.###.#####', '###.##.##.', '.###....#.', '..#.#..#.#', '#...##.#..', '', 'Tile 1171:', '####...##.', '#..##.#..#', '##.#..#.#.', '.###.####.', '..###.####', '.##....##.', '.#...####.', '#.##.####.', '####..#...', '.....##...', '', 'Tile 1427:', '###.##.#..', '.#..#.##..', '.#.##.#..#', '#.#.#.##.#', '....#...##', '...##..##.', '...#.#####', '.#.####.#.', '..#..###.#', '..##.#..#.', '', 'Tile 1489:', '##.#.#....', '..##...#..', '.##..##...', '..#...#...', '#####...#.', '#..#.#.#.#', '...#.#.#..', '##.#...##.', '..##.##.##', '###.##.#..', '', 'Tile 2473:', '#....####.', '#..#.##...', '#.##..#...', '######.#.#', '.#...#.#.#', '.#########', '.###.#..#.', '########.#', '##...##.#.', '..###.#.#.', '', 'Tile 2971:', '..#.#....#', '#...###...', '#.#.###...', '##.##..#..', '.#####..##', '.#..####.#', '#..#.#..#.', '..####.###', '..#.#.###.', '...#.#.#.#', '', 'Tile 2729:', '...#.#.#.#', '####.#....', '..#.#.....', '....#..#.#', '.##..##.#.', '.#.####...', '####.#.#..', '##.####...', '##..#.##..', '#.##...##.', '', 'Tile 3079:', '#.#.#####.', '.#..######', '..#.......', '######....', '####.#..#.', '.#...#.##.', '#.#####.##', '..#.###...', '..#.......', '..#.###...' ]

tiles = []
for line in data:
    if line == '':
        continue
    if line.startswith( "Tile" ):
        tile = line.strip(":").split(" ")[1]
        tiles.append({"name":tile, "body":[]})
    else:
        tiles[-1]["body"].append(line)

for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
         fittiles(tiles[i], tiles[j])

print( len(tiles))
