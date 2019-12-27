#!/usr/bin/env python3

"""
--- Day 11: Space Police ---
On the way to Jupiter, you're pulled over by the Space Police.

"Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible registration identifier! You have 24 hours to comply or be sent to Space Jail!"

Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three hours for their reply signal to reach you, they send instructions for how to power up the emergency hull painting robot and even provide a small Intcode program (your puzzle input) that will cause it to paint your ship appropriately.

There's just one problem: you don't have an emergency hull painting robot.

You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of square panels on the side of your ship, detect the color of its current panel, and paint its current panel black or white. (All of the panels are currently black.)

The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's camera: provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will output two values:

First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel black, and 1 means to paint the panel white.
Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
After the robot turns, it should always move forward exactly one panel. The robot starts facing up.

The robot will continue running for a while like this and halt when it is finished drawing. Do not restart the Intcode computer inside the robot during this process.

For example, suppose the robot is about to start running. Drawing black panels as ., white panels as #, and the robot pointing the direction it is facing (< ^ > v), the initial state and region near the robot looks like this:

.....
.....
..^..
.....
.....
The panel under the robot (not visible here because a ^ is shown instead) is also black, and so any input instructions at this point should be provided 0. Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left). After taking these actions and moving forward one panel, the region now looks like this:

.....
.....
.<#..
.....
.....
Input instructions should still be provided 0. Next, the robot might output 0 (paint black) and then 0 (turn left):

.....
.....
..#..
.v...
.....
After more outputs (1,0, 1,0):

.....
.....
..^..
.##..
.....
The robot is now back where it started, but because it is now on a white panel, input instructions should be provided 1. After several more outputs (0,1, 1,0, 1,0), the area looks like this:

.....
..<#.
...#.
.##..
.....
Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically, you need to know the number of panels it paints at least once, regardless of color. In the example above, the robot painted 6 panels at least once. (It painted its starting panel twice, but that panel is still only counted once; it also never painted the panel it ended on.)

Build a new emergency hull painting robot and run the Intcode program on it. How many panels does it paint at least once?
"""

from collections import deque

class Intcode:
    def __init__(self,name,data,robot):
        self.name = name
        self.d = {i:data[i] for i in range(len(data))}
        self.halted = False
        self.i = 0
        self.lastout = 0
        self.inputvals = deque([])
        self.relbase = 0
        self.robot = robot

    def stopped(self):
        return self.halted

    def lastout(self):
        return self.lastout

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

    def run(self):
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
                self.d[loc[0]] = self.robot.field.get(self.robot.pos,0)
                self.i += 2
            elif opcode == 4:
                """Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50."""
                self.lastout = self.d.get(loc[0],0)
                self.i += 2
                self.robot.command(self.lastout)
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
                return self.lastout
            else:
                print( "Unknown opcode {}".format(self.d[self.i]) )

class Robot:
    def __init__(self,field):
        self.pos = (0,0)
        self.direction = (0,-1)
        self.field = field
        self.c = None

    def command(self,c):
        if self.c == None:
            self.c = c
        else:
            self.field[self.pos] = self.c
            if c == 0:
                self.turnleft()
            elif c == 1:
                self.turnright()
            else:
                print( "Unknown turning value: {}".format(c) )
            self.c = None

    def move(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    def turnleft(self):
        if self.direction == (0,-1):
            self.direction = (-1,0)
        elif self.direction == (-1,0):
            self.direction = (0,1)
        elif self.direction == (0,1):
            self.direction = (1,0)
        elif self.direction == (1,0):
            self.direction = (0,-1)
        self.move()

    def turnright(self):
        if self.direction == (0,-1):
            self.direction = (1,0)
        elif self.direction == (1,0):
            self.direction = (0,1)
        elif self.direction == (0,1):
            self.direction = (-1,0)
        elif self.direction == (-1,0):
            self.direction = (0,-1)
        self.move()

    def printfield(self):
        maxx,maxy = 0,0
        minx,miny = 0,0
        for p in self.field:
            if minx > p[0]:
                minx = p[0]
            if maxx < p[0]:
                maxx = p[0]
            if miny > p[1]:
                miny = p[1]
            if maxy < p[1]:
                maxy = p[1]

        print(" ", end="")
        for x in range(minx-2,maxx+3):
            if x == 0:
                print("|", end="")
            else:
                print(" ", end="")
        print()
        for y in range(miny-2,maxy+3):
            if y == 0:
                print("-", end="")
            else:
                print(" ", end="")
            for x in range(minx-2,maxx+3):
                if r.pos == (x,y):
                    if r.direction == (-1,0):
                        d = "<"
                    elif r.direction == (0,1):
                        d = "v"
                    elif r.direction == (1,0):
                        d = ">"
                    elif r.direction == (0,-1):
                        d = "^"
                    print(d,end="")
                else:
                    print(self.field.get((x,y),0), end="")
            print()



with open("11.data", "r") as f:
    data = list(map(int, f.read().strip().split(",")))

r = Robot({})
painter = Intcode("paint",data,r)
painter.run()

print(len(r.field))
