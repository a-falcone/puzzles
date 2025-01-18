#!/usr/bin/env python3

"""
--- Day 24: Air Duct Spelunking ---
You've finally met your match; the doors that provide access to the roof are locked tight, and all of the controls and related electronics are inaccessible. You simply can't reach them.

The robot that cleans the air ducts, however, can.

It's not a very fast little robot, but you reconfigure it to be able to interface with some of the exposed wires that have been routed through the HVAC system. If you can direct it to each of those locations, you should be able to bypass the security controls.

You extract the duct layout for this area from some blueprints you acquired and create a map with the relevant locations marked (your puzzle input). 0 is your current location, from which the cleaning robot embarks; the other numbers are (in no particular order) the locations the robot needs to visit at least once each. Walls are marked as #, and open passages are marked as .. Numbers behave like open passages.

For example, suppose you have a map like the following:

###########
#0.1.....2#
#.#######.#
#4.......3#
###########
To reach all of the points of interest as quickly as possible, you would have the robot take the following path:

0 to 4 (2 steps)
4 to 1 (4 steps; it can't move diagonally)
1 to 2 (6 steps)
2 to 3 (2 steps)
Since the robot isn't very fast, you need to find it the shortest route. This path is the fewest steps (in the above example, a total of 14) required to start at 0 and then visit every other location at least once.

Given your actual map, and starting from location 0, what is the fewest number of steps required to visit every non-0 number marked on the map at least once?
"""

def load_data(filename: str) -> list:
    walls = set()
    locations = {}
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.rstrip()):
                if c == '#':
                    walls.add((y,x))
                elif c == '.':
                    continue
                else:
                    locations[int(c)] = (y,x)
    return walls, locations

def find_dist(start, end, walls):
    seen = set()
    queue = [(start, 0)]
    while True:
        loc, dist = queue.pop(0)
        if loc in seen:
            continue
        seen.add(loc)
        if loc == end:
            return dist
        for d in -1, 1:
            newloc = (loc[0] + d, loc[1])
            if newloc not in walls and newloc not in seen:
                queue.append((newloc, dist + 1))

            newloc = (loc[0], loc[1] + d)
            if newloc not in walls and newloc not in seen:
                queue.append((newloc, dist + 1))

def create_graph(walls, locations):
    graph = {}
    for start in locations.keys():
        for end in locations.keys():
            if start == end or (start, end) in graph:
                continue
            dist = find_dist(locations[start], locations[end], walls)
            graph[(start, end)] = dist
            graph[(end, start)] = dist
    return graph

def solve(graph, start):
    locations = set()
    for pair in graph.keys():
        locations.add(pair[0])
        locations.add(pair[1])
    locations.remove(start)
    queue = [((start,), locations.copy(), 0)]
    while True:
        visited, remaining, dist = queue.pop(0)
        if not remaining:
            return dist
        for loc in remaining:
            left = remaining.copy()
            left.remove(loc)
            queue.append((visited + (loc,), left, dist + graph[(visited[-1], loc)]))
        queue.sort(key=lambda s: s[-1])


if __name__ == "__main__":
    walls, locations = load_data("24.data")

    graph = create_graph(walls, locations)
    print(solve(graph, 0))
