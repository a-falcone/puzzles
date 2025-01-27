#!/usr/bin/env python3

"""
--- Day 11: Radioisotope Thermoelectric Generators ---
You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby. There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".

According to the project status board, this facility is currently being used to experiment with Radioisotope Thermoelectric Generators (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.

The experimental RTGs have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to generate an electromagnetic radiation shield when powered. Unfortunately, they can only be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.

In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.

These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them. The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.

Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)

You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.

When you enter the containment area, you and the elevator will start on the first floor.

For example, suppose the isolated area has the following arrangement:

The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L for Lithium, M for Microchip, and G for Generator), the initial state looks like this:

F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM
Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:

F4 .  .  .  .  .
F3 .  .  .  LG .
F2 E  HG HM .  .
F1 .  .  .  .  LM
Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:

F4 .  .  .  .  .
F3 E  HG HM LG .
F2 .  .  .  .  .
F1 .  .  .  .  LM
Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:

F4 .  .  .  .  .
F3 .  HG .  LG .
F2 E  .  HM .  .
F1 .  .  .  .  LM
At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:

F4 .  .  .  .  .
F3 .  HG .  LG .
F2 .  .  .  .  .
F1 E  .  HM .  LM
Bring both Microchips up one floor, where there is nothing to fry them:

F4 .  .  .  .  .
F3 .  HG .  LG .
F2 E  .  HM .  LM
F1 .  .  .  .  .
Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:

F4 .  .  .  .  .
F3 E  HG HM LG LM
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring both Microchips to the fourth floor:

F4 E  .  HM .  LM
F3 .  HG .  LG .
F2 .  .  .  .  .
F1 .  .  .  .  .
Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:

F4 .  .  .  .  LM
F3 E  HG HM LG .
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:

F4 E  HG .  LG LM
F3 .  .  HM .  .
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring the Lithium Microchip with you to the third floor so you can use the elevator:

F4 .  HG .  LG .
F3 E  .  HM .  LM
F2 .  .  .  .  .
F1 .  .  .  .  .
Bring both Microchips to the fourth floor:

F4 E  HG HM LG LM
F3 .  .  .  .  .
F2 .  .  .  .  .
F1 .  .  .  .  .
In this arrangement, it takes 11 steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)

In your situation, what is the minimum number of steps required to bring all of the objects to the fourth floor?

--- Part Two ---
You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.

Upon entering the isolated containment area, however, you notice some extra parts on the first floor that weren't listed on the record outside:

An elerium generator.
An elerium-compatible microchip.
A dilithium generator.
A dilithium-compatible microchip.
These work just like the other generators and microchips. You'll have to get them up to assembly as well.

What is the minimum number of steps required to bring all of the objects, including these four new ones, to the fourth floor?
"""

import re
import functools

def load_data(filename: str) -> list:
    state = (1,)
    elements = []
    with open(filename, "r") as f:
        for line in f:
            floor = list()
            for thing in re.findall(r'\w*(?:-compatible m| g)', line):
                element, machine = re.split(r' |-compatible ', thing)
                if element not in elements:
                    elements.append(element)
                element = elements.index(element) + 1
                floor.append(f'{element}{machine.upper()}')
            state += (tuple(floor),)
    return state

def is_solved(state):
    MAX_FLOOR = len(state) - 1
    if state[0] != MAX_FLOOR:
        return False
    for floor in range(1,MAX_FLOOR):
        if len(state[floor]) > 0:
            return False
    return True

@functools.cache
def is_valid_floor(floor):
    generators = [thing[0] for thing in floor if thing[1] == 'G']
    unsafe_chips = [thing[0] for thing in floor if thing[1] == 'M' and thing[0] not in generators]
    return not (len(unsafe_chips) > 0 and len(generators) > 0)

def is_valid(state):
    MAX_FLOOR = len(state) - 1
    if state[0] == 0 or state[0] > MAX_FLOOR:
        return False
    for floor in state[1:]:
        if not is_valid_floor(floor):
            return False
    return True

def move_to(original, destination, *indexes):
    original = list(original)
    destination = list(destination)
    for index in indexes:
        destination.append(original[index])
    for index in sorted(indexes, reverse=True):
        original.pop(index)
    return tuple(sorted(original)), tuple(sorted(destination))

def flatten(state):
    elevator = state[0]
    state = state[1:]
    flat = (elevator,)
    mapping = {}
    m = 0
    for floor in state:
        flat_floor = []
        for thing in floor:
            if thing[0] not in mapping:
                mapping[thing[0]] = str(m)
                m += 1
            flat_floor.append(mapping[thing[0]] + thing[1])
        flat += (tuple(sorted(flat_floor)),)
    return flat

def solve(state):
    MAX_FLOOR = len(state) - 1
    seen = set()
    queue = [(state,0)]
    while True:
        working, depth = queue.pop(0)
        if is_solved(working):
            return depth
        flat = flatten(working)
        if flat in seen:
            continue
        seen.add(flat)
        current_floor_num = working[0]
        for d in -1, 1:
            new_floor_num = current_floor_num + d
            if new_floor_num == 0 or new_floor_num > MAX_FLOOR:
                continue

            for i in range(len(working[current_floor_num])):
                working_list = list(working)
                working_list[0] = new_floor_num
                current_floor = working[current_floor_num]
                new_floor = working[new_floor_num]
                current_floor, new_floor = move_to(current_floor, new_floor, i)
                working_list[current_floor_num] = current_floor
                working_list[new_floor_num] = new_floor
                assembled = tuple(working_list)
                if is_valid(assembled):
                    queue.append((assembled, depth + 1))
                
                for j in range(i + 1, len(working[current_floor_num])):
                    working_list = list(working)
                    working_list[0] = new_floor_num
                    current_floor = working[current_floor_num]
                    new_floor = working[new_floor_num]
                    current_floor, new_floor = move_to(current_floor, new_floor, i, j)
                    working_list[current_floor_num] = current_floor
                    working_list[new_floor_num] = new_floor
                    assembled = tuple(working_list)
                    if is_valid(assembled):
                        queue.append((assembled, depth + 1))


if __name__ == "__main__":
    state = load_data("11.data2")

    print(solve(state))
