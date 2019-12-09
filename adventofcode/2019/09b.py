#!/usr/bin/env python3

"""
--- Day 9: Sensor Boost ---
You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress signal coming from the asteroid belt. It must be the Ceres monitoring station!

In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest BOOST program - Basic Operation Of System Test.

While BOOST (your puzzle input) is capable of boosting your sensors, for tenuous safety reasons, it refuses to do so until the computer it runs on passes some checks to demonstrate it is a complete Intcode computer.

Your existing Intcode computer is missing one key feature: it needs support for parameters in relative mode.

Parameters in mode 2, relative mode, behave very similarly to parameters in position mode: the parameter is interpreted as a position. Like position mode, parameters in relative mode can be read from or written to.

The important difference is that relative mode parameters don't count from address 0. Instead, they count from a value called the relative base. The relative base starts at 0.

The address a relative mode parameter refers to is itself plus the current relative base. When the relative base is 0, relative mode parameters and position mode parameters with the same value refer to the same address.

For example, given a relative base of 50, a relative mode parameter of -7 refers to memory address 50 + -7 = 43.

The relative base is modified with the relative base offset instruction:

Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.
For example, if the relative base is 2000, then after the instruction 109,19, the relative base would be 2019. If the next instruction were 204,-34, then the value at address 1985 would be output.

Your Intcode computer will also need a few other capabilities:

The computer's available memory should be much larger than the initial program. Memory beyond the initial program starts with the value 0 and can be read or written like any other memory. (It is invalid to try to access memory at a negative address, though.)
The computer should have support for large numbers. Some instructions near the beginning of the BOOST program will verify this capability.
Here are some example programs that use these features:

109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy of itself as output.
1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
104,1125899906842624,99 should output the large number in the middle.
The BOOST program will ask for a single input; run it in test mode by providing it the value 1. It will perform a series of checks on each opcode, output any opcodes (and the associated parameter modes) that seem to be functioning incorrectly, and finally output a BOOST keycode.

Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning opcodes when run in test mode; it should only output a single value, the BOOST keycode. What BOOST keycode does it produce?

--- Part Two ---
You now have a complete Intcode computer.

Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using the BOOST program.

The program runs in sensor boost mode by providing the input instruction the value 2. Once run, it will boost the sensors automatically, but it might take a few seconds to complete the operation on slower hardware. In sensor boost mode, the program will output a single value: the coordinates of the distress signal.

Run the BOOST program in sensor boost mode. What are the coordinates of the distress signal?
"""

import itertools
from collections import deque

class Intcode:
    def __init__(self,name,data):
        self.name = name
        self.d = {i:data[i] for i in range(len(data))}
        self.halted = False
        self.i = 0
        self.lastout = 0
        self.inputvals = deque([])
        self.relbase = 0

    def stopped(self):
        return self.halted

    def lastout(self):
        return self.lastout

    def locations(self,modes):
        ls = []
        """0: position mode
           1: immediate mode
           2: relative mode
        """
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

    def run(self,inputvals):
        self.inputvals.extend(inputvals)
        if self.halted:
            print( "Amp {} is halted. Can not run.".format(self.name) )
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
                self.d[loc[0]] = self.inputvals.popleft()
                self.i += 2
            elif opcode == 4:
                """Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50."""
                self.lastout = self.d.get(loc[0],0)
                print(self.lastout)
                self.i += 2
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

with open("09.data", "r") as f:
  data = list(map(int, f.read().strip().split(",")))

Intcode("BOOST", data).run([2])
