#!/usr/bin/env pypy3

"""
--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(list(map(int,list(line.rstrip()))))
    return data

if __name__ == "__main__":
    trees = load_data("08.data")
    lvis, rvis = set([(i,0) for i in range(len(trees))]), set([(i,len(trees)-1) for i in range(len(trees))])
    for row in range(len(trees)):
        lmax = trees[row][0]
        for col in range(1,len(trees[row])):
            if trees[row][col] > lmax:
                lvis.add((row,col))
                lmax = trees[row][col]

        rmax = trees[row][-1]
        for col in range(len(trees[row]) - 2, -1, -1):
            if trees[row][col] > rmax:
                rvis.add((row,col))
                rmax = trees[row][col]
        
    uvis, dvis = set([(0,i) for i in range(len(trees[0]))]), set([(len(trees[0])-1,i) for i in range(len(trees[0]))])
    for col in range(len(trees[0])):
        umax = trees[0][col]
        for row in range(1,len(trees)):
            if trees[row][col] > umax:
                uvis.add((row,col))
                umax = trees[row][col]

        dmax = trees[len(trees)-1][col]
        for row in range(len(trees) - 2, -1, -1):
            if trees[row][col] > dmax:
                dvis.add((row,col))
                dmax = trees[row][col]

    vis = set()
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            t = (row,col)
            if t in rvis or t in lvis or t in uvis or t in dvis:
                vis.add(t)
    print(len(vis))
