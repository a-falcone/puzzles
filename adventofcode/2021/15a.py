#!/usr/bin/env python3

"""
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
"""

def dijkstra(vertices, edges, source, end):
    #https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
    unvisited = set(vertices)
    dist = {}
    for p in unvisited:
        dist[p] = float("inf")

    dist[source] = 0

    while unvisited:
        minp, minv = None, float("inf")
        for p in unvisited:
            if dist[p] < minv:
                minp = p
                minv = dist[p]

        if minp == end:
            return dist

        unvisited.remove(minp)

        for neighbor in edges[minp].keys():
            if neighbor in unvisited:
                test = dist[minp] + edges[minp][neighbor]
                if test < dist[neighbor]:
                    dist[neighbor] = test

    return dist

def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.strip())
    return data

if __name__ == "__main__":
    data = load_data("15.data")

    risk = [[int(c) for c in line] for line in data]
    
    vertices = set()
    edges = {}
    for y in range(len(risk)):
        for x in range(len(risk[y])):
            p = (x,y)
            vertices.add(p)
            for dx, dy in (1,0), (0,1), (-1,0), (0,-1):
                if 0 <= x+dx < len(risk[y]) and 0 <= y+dy < len(risk):
                    p2 = (x+dx,y+dy)
                    edges[p] = edges.get(p, {})
                    edges[p][p2] = risk[y+dy][x+dx]
                    edges[p2] = edges.get(p2, {})
                    edges[p2][p] = risk[y][x]

    end = (len(risk[-1]) - 1, len(risk) - 1)
    distance = dijkstra(vertices, edges, (0,0), end)
    print(distance[end])
