#!/usr/bin/env python3

"""
--- Day 17: Set and Forget ---
An early warning system detects an incoming solar flare and automatically activates the ship's electromagnetic shield. Unfortunately, this has cut off the Wi-Fi for many small robots that, unaware of the impending danger, are now trapped on exterior scaffolding on the unsafe side of the shield. To rescue them, you'll have to act quickly!

The only tools at your disposal are some wired cameras and a small vacuum robot currently asleep at its charging station. The video quality is poor, but the vacuum robot has a needlessly bright LED that makes it easy to spot no matter where it is.

An Intcode program, the Aft Scaffolding Control and Information Interface (ASCII, your puzzle input), provides access to the cameras and the vacuum robot. Currently, because the vacuum robot is asleep, you can only access the cameras.

Running the ASCII program on your Intcode computer will provide the current view of the scaffolds. This is output, purely coincidentally, as ASCII code: 35 means #, 46 means ., 10 starts a new line of output below the current one, and so on. (Within a line, characters are drawn left-to-right.)

In the camera output, # represents a scaffold and . represents open space. The vacuum robot is visible as ^, v, <, or > depending on whether it is facing up, down, left, or right respectively. When drawn like this, the vacuum robot is always on a scaffold; if the vacuum robot ever walks off of a scaffold and begins tumbling through space uncontrollably, it will instead be visible as X.

In general, the scaffold forms a path, but it sometimes loops back onto itself. For example, suppose you can see the following view from the cameras:

..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
Here, the vacuum robot, ^ is facing up and sitting at one end of the scaffold near the bottom-right of the image. The scaffold continues up, loops across itself several times, and ends at the top-left of the image.

The first step is to calibrate the cameras by getting the alignment parameters of some well-defined points. Locate all scaffold intersections; for each, its alignment parameter is the distance between its left edge and the left edge of the view multiplied by the distance between its top edge and the top edge of the view. Here, the intersections from the above image are marked O:

..#..........
..#..........
##O####...###
#.#...#...#.#
##O###O###O##
..#...#...#..
..#####...^..
For these intersections:

The top-left intersection is 2 units from the left of the image and 2 units from the top of the image, so its alignment parameter is 2 * 2 = 4.
The bottom-left intersection is 2 units from the left and 4 units from the top, so its alignment parameter is 2 * 4 = 8.
The bottom-middle intersection is 6 from the left and 4 from the top, so its alignment parameter is 24.
The bottom-right intersection's alignment parameter is 40.
To calibrate the cameras, you need the sum of the alignment parameters. In the above example, this is 76.

Run your ASCII program. What is the sum of the alignment parameters for the scaffold intersections?
"""

from os import system

class Intcode:
    def __init__(self,name,data):
        self.name = name
        self.d = {i:data[i] for i in range(len(data))}
        self.halted = False
        self.i = 0
        self.lastout = 0
        self.relbase = 0

    def locations(self,modes):
        ls = []
        """0: position mode
           1: immediate mode
           2: relative mode """
        for x in range(1,4):
            if modes % 10 == 0:
                ls.append(self.d.get(self.i + x, 0))
            elif modes % 10 == 1:
                ls.append(self.i + x)
            elif modes % 10 == 2:
                ls.append(self.d.get(self.i + x, 0) + self.relbase)
            else:
                print("Unknown mode in {}".format(modes))
            modes //= 10
        return ls

    def run(self, command):
        if self.halted:
            print( "{} is halted. Can not run.".format(self.name) )
            return False

        while True:
            opcode, loc = self.d[self.i] % 100, self.locations(self.d[self.i] // 100)
            if opcode == 1:
                """Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored."""
                self.d[loc[2]] = self.d.get(loc[0],0) + self.d.get(loc[1],0)
                self.i += 4
            elif opcode == 2:
                """Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values."""
                self.d[loc[2]] = self.d.get(loc[0],0) * self.d.get(loc[1],0)
                self.i += 4
            elif opcode == 3:
                """Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50."""
                if command == None:
                    return None
                self.d[loc[0]] = command
                self.i += 2
            elif opcode == 4:
                """Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50."""
                self.lastout = self.d.get(loc[0],0)
                self.i += 2
                return(self.lastout)
            elif opcode == 5:
                """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""
                if self.d.get(loc[0],0):
                  self.i = self.d.get(loc[1],0)
                else:
                  self.i += 3
            elif opcode == 6:
                """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""
                if self.d.get(loc[0],0):
                  self.i += 3
                else:
                  self.i = self.d.get(loc[1],0)
            elif opcode == 7:
                """Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
                self.d[loc[2]] = 1 if self.d.get(loc[0],0) < self.d.get(loc[1],0) else 0
                self.i += 4
            elif opcode == 8:
                """Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
                self.d[loc[2]] = 1 if self.d.get(loc[0],0) == self.d.get(loc[1],0) else 0
                self.i += 4
            elif opcode == 9:
                """Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter."""
                self.relbase += self.d.get(loc[0],0)
                self.i += 2
            elif opcode == 99:
                self.halted = True
                return None
            else:
                print( "Unknown opcode {}".format(self.d[self.i]) )

with open("17.data", "r") as f:
    data = list(map(int, f.read().strip().split(",")))

computer = Intcode("c",data)

field = ""

out = computer.run(None)
while out is not None:
    field += chr(out)
    out = computer.run(None)

grid = [list(i) for i in field.split()]

sum = 0
for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        if grid[y][x] == "#" and\
           grid[y+1][x] == "#" and\
           grid[y-1][x] == "#" and\
           grid[y][x+1] == "#" and\
           grid[y][x-1] == "#":
            sum += x*y

print(sum)

