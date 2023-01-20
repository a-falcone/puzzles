#!/usr/bin/env python3

"""
--- Day 21: Monkey Math ---
The monkeys are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding their ground and making various monkey noises at you.

Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard you talking about trying to find the grove; they can show you a shortcut if you answer their riddle.

Each monkey is given a job: either to yell a specific number or to yell the result of a math operation. All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait for two other monkeys to yell a number, and those two other monkeys might also be waiting on other monkeys.

Your job is to work out the number the monkey named root will yell before the monkeys figure it out themselves.

For example:

root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
Each line contains the name of a monkey, a colon, and then the job of that monkey:

A lone number means the monkey's job is simply to yell that number.
A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to yell each of their numbers; the monkey then yells the sum of those two numbers.
aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.
So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc to yell their numbers. Fortunately, both hmdt and zczc have jobs that involve simply yelling a single number, so they do this immediately: 32 and 2. Monkey drzm can then yell its number by finding 32 minus 2: 30.

Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already has its other number, 5, from dbpl. This allows it to yell its own number by finding 30 multiplied by 5: 150.

This process continues until root yells a number: 152.

However, your actual situation involves considerably more monkeys. What number will the monkey named root yell?

--- Part Two ---
Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named root; specifically, you got the wrong math operation. The correct operation for monkey root should be =, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers match.

Second, you got the wrong monkey for the job starting with humn:. It isn't a monkey - it's you. Actually, you got the job wrong, too: you need to figure out what number you need to yell so that root's equality check passes. (The number that appears after humn: in your input is now irrelevant.)

In the above example, the number you need to yell to pass root's equality test is 301. (This causes root to get the same number, 150, from both of its monkeys.)

What number do you yell to pass root's equality test?
"""

seen = set()

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.rstrip())
    return data

def compute(tokens: list, numbers: dict) -> int:
    val1 = int(numbers[tokens[0]])
    val2 = int(numbers[tokens[2]])
    op = tokens[1]
    if op == "+":
        return val1 + val2
    elif op == "-":
        return val1 - val2
    elif op == "*":
        return val1 * val2
    elif op == "/":
        return val1 // val2

def make_equation(tokens: list, numbers: dict, current: str):
    a, op, b = tokens
    if b == current:
        a = numbers[a]
        if op == "+":
            #c = a + eqtn -> eqtn = c - a
            return lambda c: c - a
        elif op == "-":
            #c = a - eqtn -> eqtn = a - c
            return lambda c: a - c
        elif op == "*":
            #c = a * eqtn -> eqtn = c / a
            return lambda c: c // a
        elif op == "/":
            #c = a / eqtn -> eqtn = a / c
            return lambda c: a // c
    else:
        b = numbers[b]
        if op == "+":
            #c = eqtn + b -> eqtn = c - b
            return lambda c: c - b
        elif op == "-":
            #c = eqtn - b -> eqtn = c + b
            return lambda c: c + b
        elif op == "*":
            #c = eqtn * b -> eqtn = c / b
            return lambda c: c // b
        elif op == "/":
            #c = eqtn / b -> eqtn = c * b
            return lambda c: c * b
    

if __name__ == "__main__":
    data = load_data("21.data")
    #data = load_data("21.test")

    numbers = {}
    equations = []
    monkeys = {}
    current = "humn"
    for line in data:
        monkey, rest = line.split(": ")
        if monkey == "humn":
            continue
        tokens = rest.split(" ")
        if monkey == "root":
            root = (tokens[0], tokens[2])
        if len(tokens) == 1:
            numbers[monkey] = int(tokens[0])
        else:
            monkeys[monkey] = tokens

    while current != "root":
        if (root[0] in numbers and root[1] in equations) or (root[1] in numbers and root[0] in equations):
               break
        for monkey, tokens in monkeys.items():
            if tokens[0] in numbers and tokens[2] in numbers:
                numbers[monkey] = compute(tokens, numbers)
            elif (tokens[0] == current and tokens[2] in numbers) or (tokens[2] == current and tokens[0] in numbers):
                if monkey == "root":
                    current = "root"
                    break
                equations.append(make_equation(tokens, numbers, current))
                current = monkey
                
    if root[0] in numbers:
        number = numbers[root[0]]
    else:
        number = numbers[root[1]]
    for l in equations[::-1]:
        number = l(number)
    print(number)
