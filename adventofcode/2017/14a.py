#!/usr/local/bin/python3

"""
Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#   
....#.#.   
#.#.##.#   
.##.#...   
##..#..#   
.#...#..   
##.#.##.-->
|      |   
V      V   

In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

Your puzzle input is jxqlasbh.
"""

import re

testdata="flqrgnkx"
data="jxqlasbh"

def knothash( instring ):
    s = [ord(l) for l in instring]
    s.append(17)
    s.append(31)
    s.append(73)
    s.append(47)
    s.append(23)
    a = [i for i in range(256)]
    pos = skip = 0

    for _ in range(64):
        for l in s:
            end = (pos + l - 1) % len( a )
            for i in range(0, l // 2):
                a[end - i], a[end - l + 1 + i] = a[end - l + 1 + i], a[end - i]

            pos += (l + skip) % len( a )
            skip += 1
    dense=""

    for i in range(16):
        temp = 0
        for j in range(16):
            temp ^= a[16*i + j]
        dense += "%8s" % format(temp, 'b')

        dense = re.sub("[ 0]", ".", dense)
        dense = re.sub("1", "#", dense)

    return dense

count = 0
for i in range(128):
    hashed = knothash(data + "-" + str(i))
    count += hashed.count("#")
    
print( count )
