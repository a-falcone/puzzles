#!/usr/bin/env python3

"""
--- Day 8: Space Image Format ---
The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.

Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.

Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
"""

def load(d,w,h):
    layers = []
    for i in range(len(d)):
        l = i // (w*h)
        x = i % w
        y = (i // w) % h 
        if x == 0 and y == 0:
            layers.append([[None for i in range(w)] for j in range(h)])
        layers[l][y][x] = d[i]
    return layers

width,height = 25, 6

with open("08.data", "r") as f:
    data = list(f.read().strip())

layers = load(data,width,height)

prod = 0
min0 = width*height + 1
for l in layers:
    temp1 = 0
    temp2 = 0
    num0 = 0
    for y in l:
        num0 += y.count("0")
        temp1 += y.count("1")
        temp2 += y.count("2")
    if num0 < min0:
        prod = temp1 * temp2
        min0 = num0

print(prod)
