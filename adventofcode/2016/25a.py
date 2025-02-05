#!/usr/bin/env python3

"""
--- Day 25: Clock Signal ---
You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.

There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.

However, maybe the huge antenna up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.

You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.

Nothing happens.

You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.

"No, no, a clock signal - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.

You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's no way it can! The only antenna we've installed capable of that is on top of a top-secret Easter Bunny installation, and you're definitely not-" You hang up the phone.

You've extracted the antenna's clock signal generation assembunny code (your puzzle input); it looks mostly compatible with code you worked on just recently.

This antenna code, being a signal generator, uses one extra instruction:

out x transmits x (either an integer or the value of a register) as the next value for the clock signal.
The code takes a value (via register a) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.

What is the lowest positive integer that can be used to initialize register a and cause the code to output a clock signal of 0, 1, 0, 1... repeating forever?
"""

def load_data(filename: str) -> list:
    instructions = []
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            line = tuple(line.split())
            instructions.append(line)
    return tuple(instructions)

def run_once(a, instructions):
    def value(reg, x):
        if x in reg:
            return reg[x]
        else:
            return int(x)

    reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    pointer = 0
    expected = 0
    while True:
        instruction = instructions[pointer]
        if instruction[0] == 'cpy':
            reg[instruction[2]] = value(reg, instruction[1])
        elif instruction[0] == 'inc':
            reg[instruction[1]] += 1
        elif instruction[0] == 'dec':
            reg[instruction[1]] -= 1
        elif instruction[0] == 'jnz':
            if value(reg, instruction[1]) != 0:
                pointer += int(instruction[2])
                continue
        elif instruction[0] == 'out':
            if value(reg, instruction[1]) != expected:
                return
            expected = 1 - expected

        pointer += 1



if __name__ == "__main__":
    instructions = load_data("25.data")

    answer = 0
    while True:
        print(f"Working on {answer}...")
        run_once(answer, instructions)
        print("Failed.")
        answer += 1
