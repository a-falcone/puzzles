#!/usr/bin/env python3

"""
--- Day 15: Oxygen System ---
Out here in deep space, many things can go wrong. Fortunately, many of those things have indicator lights. Unfortunately, one of those lights is lit: the oxygen system for part of the ship has failed!

According to the readouts, the oxygen system must have failed days ago after a rupture in oxygen tank two; that section of the ship was automatically sealed once oxygen levels went dangerously low. A single remotely-operated repair droid is your only option for fixing the oxygen system.

The Elves' care package included an Intcode program (your puzzle input) that you can use to remotely control the repair droid. By running that program, you can direct the repair droid to the oxygen system and fix the problem.

The remote control program executes the following steps in a loop forever:

Accept a movement command via an input instruction.
Send the movement command to the repair droid.
Wait for the repair droid to finish the movement operation.
Report on the status of the repair droid via an output instruction.
Only four movement commands are understood: north (1), south (2), west (3), and east (4). Any other command is invalid. The movements differ in direction, but not in distance: in a long enough east-west hallway, a series of commands like 4,4,4,4,3,3,3,3 would leave the repair droid back where it started.

The repair droid can reply with any of the following status codes:

0: The repair droid hit a wall. Its position has not changed.
1: The repair droid has moved one step in the requested direction.
2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
You don't know anything about the area around the repair droid, but you can figure it out by watching the status codes.

For example, we can draw the area using D for the droid, # for walls, . for locations the droid can traverse, and empty space for unexplored locations. Then, the initial state looks like this:



   D


To make the droid go north, send it 1. If it replies with 0, you know that location is a wall and that the droid didn't move:


   #
   D


To move east, send 4; a reply of 1 means the movement was successful:


   #
   .D


Then, perhaps attempts to move north (1), south (2), and east (4) are all met with replies of 0:


   ##
   .D#
    #

Now, you know the repair droid is in a dead end. Backtrack with 3 (which you already know will get a reply of 1 because you already know that location is open):


   ##
   D.#
    #

Then, perhaps west (3) gets a reply of 0, south (2) gets a reply of 1, south again (2) gets a reply of 0, and then west (3) gets a reply of 2:


   ##
  #..#
  D.#
   #
Now, because of the reply of 2, you know you've found the oxygen system! In this example, it was only 2 moves away from the repair droid's starting position.

What is the fewest number of movement commands required to move the repair droid from its starting position to the location of the oxygen system?

--- Part Two ---
You quickly repair the oxygen system; oxygen gradually fills the area.

Oxygen starts in the location containing the repaired oxygen system. It takes one minute for oxygen to spread to all open locations that are adjacent to a location that already contains oxygen. Diagonal locations are not adjacent.

In the example above, suppose you've used the droid to explore the area fully and have the following map (where locations that currently contain oxygen are marked O):

 ##
#..##
#.#..#
#.O.#
 ###
Initially, the only location which contains oxygen is the location of the repaired oxygen system. However, after one minute, the oxygen spreads to all open (.) locations that are adjacent to a location containing oxygen:

 ##
#..##
#.#..#
#OOO#
 ###
After a total of two minutes, the map looks like this:

 ##
#..##
#O#O.#
#OOO#
 ###
After a total of three minutes:

 ##
#O.##
#O#OO#
#OOO#
 ###
And finally, the whole region is full of oxygen after a total of four minutes:

 ##
#OO##
#O#OO#
#OOO#
 ###
So, in this example, all locations contain oxygen after 4 minutes.

Use the repair droid to get a complete map of the area. How many minutes will it take to fill with oxygen?
"""

from os import system
import random

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

class Ship:
    def __init__(self):
        self.pos = (0,0)
        self.field = {self.pos: 0}
        self.maxx, self.minx, self.maxy, self.miny = 0,0,0,0
        self.found = False
        self.maxdepth = 0

    def __repr__(self):
        out = ""
        for y in range(self.miny-2,self.maxy+3):
            for x in range(self.minx-2,self.maxx+3):
                if self.pos == (x,y):
                    out += "D"
                elif (x,y) == (0,0):
                    out += "s"
                elif self.field.get((x,y),-1) == -1:
                    out += " "
                elif self.field.get((x,y),-1) == 0:
                    out += "#"
                elif self.field.get((x,y),-1) == 1:
                    out += "."
                elif self.field.get((x,y),-1) == 2:
                    out += "O"
            out += "\n"
        return out

    def newpos(self, d):
        if d == 1:
            if self.miny == self.pos[1]:
                self.miny -= 1
            newpos = (self.pos[0],self.pos[1] - 1)
        elif d == 2:
            if self.maxy == self.pos[1]:
                self.maxy += 1
            newpos = (self.pos[0],self.pos[1] + 1)
        elif d == 3:
            if self.minx == self.pos[0]:
                self.minx -= 1
            newpos = (self.pos[0] - 1,self.pos[1])
        elif d == 4:
            if self.maxx == self.pos[0]:
                self.maxx += 1
            newpos = (self.pos[0] + 1,self.pos[1])
        else:
            print("{} is an invalid direction".format(d))
            return None
        return newpos

    def move(self, d, computer):
        newpos = self.newpos(d)

        out = computer.run(d)
        if out == 0: #wall
            ship.field[newpos] = 0
        elif out == 1: #free
            ship.pos = newpos
            ship.field[ship.pos] = 1
        elif out == 2: #tank
            ship.pos = newpos
            ship.field[ship.pos] = 2
            #print("FOUND IT")
            #input()
        else:
            print( "Got something weird: {}".format(out))
            #input()
        return out

OPP = [None, 2, 1, 4, 3]

def run(depth, ship, computer):
    if ship.field[ship.pos] == 2:
        ship.found = True
        return None
    for direction in [4,3,1,2]:
        if ship.found:
            return None
        newpos = ship.newpos(direction)
        if newpos not in ship.field:
            out = ship.move(direction,computer)
            if out != 0:
                run(depth + 1, ship, computer)
                if ship.found:
                    return None
                ship.move(OPP[direction],computer)

def runagain(depth, ship, computer):
    ship.maxdepth = max(depth, ship.maxdepth)
    for direction in [4,3,1,2]:
        newpos = ship.newpos(direction)
        if newpos not in ship.field:
            out = ship.move(direction,computer)
            if out != 0:
                runagain(depth + 1, ship, computer)
                ship.move(OPP[direction],computer)

with open("15.data", "r") as f:
    data = list(map(int, f.read().strip().split(",")))

computer = Intcode("c",data)

ship = Ship()
run(0, ship, computer)

ship = Ship()
runagain(0,ship,computer)
print(ship.maxdepth)
