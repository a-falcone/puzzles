#!/usr/bin/env python3

"""
--- Day 13: Care Package ---
As you ponder the solitude of space and the ever-increasing three-hour roundtrip for messages between you and Earth, you notice that the Space Mail Indicator Light is blinking. To help keep you sane, the Elves have sent you a care package.

It's a new game for the ship's arcade cabinet! Unfortunately, the arcade is all the way on the other end of the ship. Surely, it won't be hard to build your own - the care package even comes with schematics.

The arcade cabinet runs Intcode software like the game the Elves sent (your puzzle input). It has a primitive screen capable of drawing square tiles on a grid. The software draws tiles to the screen with output instructions: every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id. The tile id is interpreted as follows:

0 is an empty tile. No game object appears in this tile.
1 is a wall tile. Walls are indestructible barriers.
2 is a block tile. Blocks can be broken by the ball.
3 is a horizontal paddle tile. The paddle is indestructible.
4 is a ball tile. The ball moves diagonally and bounces off objects.
For example, a sequence of output values like 1,2,3,6,5,4 would draw a horizontal paddle tile (1 tile from the left and 2 tiles from the top) and a ball tile (6 tiles from the left and 5 tiles from the top).

Start the game. How many block tiles are on the screen when the game exits?

--- Part Two ---
The game didn't run because you didn't put in any quarters. Unfortunately, you did not bring any quarters. Memory address 0 represents the number of quarters that have been inserted; set it to 2 to play for free.

The arcade cabinet has a joystick that can move left and right. The software reads the position of the joystick with input instructions:

If the joystick is in the neutral position, provide 0.
If the joystick is tilted to the left, provide -1.
If the joystick is tilted to the right, provide 1.
The arcade cabinet also has a segment display capable of showing a single number that represents the player's current score. When three output instructions specify X=-1, Y=0, the third output instruction is not a tile; the value instead specifies the new score to show in the segment display. For example, a sequence of output values like -1,0,12345 would show 12345 as the player's current score.

Beat the game by breaking all the blocks. What is your score after the last block is broken?
"""

from collections import deque
from os import system
import time

class Intcode:
    def __init__(self,name,data):
        self.name = name
        self.d = {i:data[i] for i in range(len(data))}
        self.halted = False
        self.i = 0
        self.lastout = 0
        self.relbase = 0

    def copy(self):
        c = Intcode(self.name+"_copy", self.d.copy())
        c.halted = self.halted
        c.i = self.i
        c.lastout = self.lastout
        c.relbase = self.relbase
        return c

    def stopped(self):
        return self.halted

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
                return self.lastout
            else:
                print( "Unknown opcode {}".format(self.d[self.i]) )

class Game:
    def __init__(self):
        self.grid = {}
        self.maxx = 0
        self.maxy = 0
        self.ballloc = (0,0)
        self.paddleloc = (0,0)
        self.c = []

    def copy(self):
        g = Game()
        g.grid = self.grid.copy()
        g.maxx = self.maxx
        g.maxy = self.maxy
        g.ballloc = tuple(self.ballloc)
        g.paddleloc = tuple(self.paddleloc)
        g.c = self.c.copy()
        return g

    def bricks(self):
        count = 0
        for i in self.grid:
            if self.grid[i] == 2:
                count += 1
        return count

    def score(self):
        return self.grid.get((-1,0), 0)

    def __repr__(self):
        output = "Score: {}\n\n".format(self.grid.get((-1,0), "Unknown"))
        for y in range(self.maxy+1):
            for x in range(self.maxx+1):
                c = self.grid.get((x,y),0)
                if c == 0:
                    output += " "
                elif c == 1:
                    output += "#"
                elif c == 2:
                    output += "x"
                elif c == 3:
                    output += "_"
                elif c == 4:
                    output += "o"
            output += "\n"
        print("Ball: {}, paddle: {}".format(self.ballloc, self.paddleloc))
        return output

    def command(self, c):
        self.c.append(c)
        if len(self.c) == 3:
            if c == 3:
                self.paddleloc = (self.c[0], self.c[1])
            elif c == 4:
                self.ballloc = (self.c[0], self.c[1])
            self.maxx = max(self.maxx, self.c[0])
            self.maxy = max(self.maxy, self.c[1])
            self.grid[(self.c[0], self.c[1])] = self.c[2]
            self.c = []

with open("13.data", "r") as f:
    data = list(map(int, f.read().strip().split(",")))
data[0] = 2

game = Game()
computer = Intcode("game",data)
nextcommand = None
uninitialized = True
while uninitialized or game.bricks() > 0:
    out = computer.run(nextcommand)
    nextcommand = None
    if out == None:
        uninitialized = False
#        system('clear')
#        print("Remaining bricks: {}".format(game.bricks()))
#        print(game)
        if game.paddleloc[0] == game.ballloc[0] and game.paddleloc[1] == game.ballloc[1] + 1:
            nextcommand = 0
        else:
            og = game.copy()
            oc = computer.copy()
            on = 0
            oout = oc.run(on)
            while not oc.halted and not oout == None:
                og.command(oout)
                oout = oc.run(None)
            if og.paddleloc[0] > og.ballloc[0]:
                nextcommand = -1
            elif og.paddleloc[0] == og.ballloc[0]:
                nextcommand = 0
            elif og.paddleloc[0] < og.ballloc[0]:
                nextcommand = 1
    else:
        game.command(int(out))

computer.run(None)
computer.run(None)
print(computer.run(None))
