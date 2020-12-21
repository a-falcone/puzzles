#!/usr/bin/env pypy3

"""
"""

import re

data = []

with open("21.data", "r") as f:
    for line in f:
        data.append(line.strip())

#data = [ 'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)', 'trh fvjkl sbzzf mxmxvkd (contains dairy)', 'sqjhc fvjkl (contains soy)', 'sqjhc mxmxvkd sbzzf (contains fish)' ]

ingredients = set()
foods = {}
for line in data:
    m = re.fullmatch( "(.*) \(contains (.*)\)", line )
    ings = set(m.group(1).split(" "))
    fs = m.group(2).split(", ")
    for i in ings:
        ingredients.add(i)
        for f in fs:
            if f not in foods:
                foods[f] = ings
            else:
                foods[f] = foods[f].intersection( ings )

print( foods )

for i in ingredients.copy():
    keep = True
    for v in foods.values():
        if i in v:
            keep = False
    if not keep:
        ingredients.remove( i )

count = 0
print( ingredients)
for i in ingredients:
    for line in data:
        m = re.fullmatch( "(.*) \(contains (.*)\)", line )
        if i in m.group(1):
            count += 1
print( count )
