#!/usr/bin/env pypy3

"""
--- Day 18: Boiling Boulders ---
You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming obsidian! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side covered and five sides exposed, a total surface area of 10 sides.

Here's a larger example:

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is 64.

What is the surface area of your scanned lava droplet?
"""

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.rstrip())
    return data

if __name__ == "__main__":
    data = load_data("18.data")

    seen = set()
    touching = set()

    for line in data:
        x,y,z = map(int,line.split(","))

        #right
        if (x+1,y,z,"l") in seen:
            seen.remove((x+1,y,z,"l"))
            touching.add((x+1,y,z,"l"))
            touching.add((x,y,z,"r"))
        else:
            seen.add((x,y,z,"r"))

        #left
        if (x-1,y,z,"r") in seen:
            seen.remove((x-1,y,z,"r"))
            touching.add((x-1,y,z,"r"))
            touching.add((x,y,z,"l"))
        else:
            seen.add((x,y,z,"l"))

        #front
        if (x,y+1,z,"b") in seen:
            seen.remove((x,y+1,z,"b"))
            touching.add((x,y+1,z,"b"))
            touching.add((x,y,z,"f"))
        else:
            seen.add((x,y,z,"f"))

        #back
        if (x,y-1,z,"f") in seen:
            seen.remove((x,y-1,z,"f"))
            touching.add((x,y-1,z,"f"))
            touching.add((x,y,z,"b"))
        else:
            seen.add((x,y,z,"b"))

        #up
        if (x,y,z+1,"d") in seen:
            seen.remove((x,y,z+1,"d"))
            touching.add((x,y,z+1,"d"))
            touching.add((x,y,z,"u"))
        else:
            seen.add((x,y,z,"u"))

        #down
        if (x,y,z-1,"u") in seen:
            seen.remove((x,y,z-1,"u"))
            touching.add((x,y,z-1,"u"))
            touching.add((x,y,z,"d"))
        else:
            seen.add((x,y,z,"d"))

    print(len(seen))
