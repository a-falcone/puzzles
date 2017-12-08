#!/usr/local/bin/python3

"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

        b inc 5 if a > 1
        a inc 1 if b < 5
        c dec -10 if a >= 1
        c inc -20 if c == 10

These instructions would be processed as follows:

        Because a starts at 0, it is not greater than 1, and so b is not modified.
        a is increased by 1 (to 1) because b is less than 5 (it is 0).
        c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
        c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?
"""

reg = {}

f = open("data/08.data", "r")

for line in f.readlines():
    modreg, mod, modamount, _, compreg, comp, compamount = line.split()
    if modreg not in reg:
        reg[modreg] = 0
    if compreg not in reg:
        reg[compreg] = 0
    modamount = int(modamount)
    compamount = int(compamount)
    evalstr = "%d %s %d" % (reg[compreg], comp, compamount)
    if eval(evalstr):
        if mod == "inc":
            reg[modreg] += modamount
        else:
            reg[modreg] -= modamount

maxval, maxreg = -9999999, ""
for key in reg.keys():
    if reg[key] > maxval:
        maxval = reg[key]
        maxreg = key

print(maxreg, maxval)
