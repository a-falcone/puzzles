#!/usr/bin/env python3

"""
--- Day 18: Snailfish ---
You descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his math homework.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as [x,y], where x and y are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

If any pair is nested inside four pairs, the leftmost such pair explodes.
If any regular number is 10 or greater, the leftmost such regular number splits.
Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

Here are some examples of a single explode action:

[[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
[7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
[[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

Here is the process of finding the reduced result of [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]:

after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: [[[[0,7],4],[[7,8],[6,0]]],[8,1]].

The homework assignment involves adding up a list of snailfish numbers (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:

[1,1]
[2,2]
[3,3]
[4,4]
The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
Here's a slightly larger example:

[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
The final sum [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] is found after adding up the above snailfish numbers:

  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9] is 3*1 + 2*9 = 21. Magnitude calculations are recursive: the magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.

Here are a few more magnitude examples:

[[1,2],[[3,4],5]] becomes 143.
[[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
[[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
[[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
[[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
So, given this example homework assignment:

[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
The final sum is:

[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
The magnitude of this final sum is 4140.

Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?
"""

import json
from math import floor, ceil

class Snum:
    def __init__(self, s, leaf, parent):
        self.left, self.right = None, None
        self.leaf = leaf
        self.parent = parent

        if type(parent) is not Snum and parent is not None:
            raise TypeError(f"Parent issues: {parent=}")

        if type(s) is not list or len(s) != 2:
            raise TypeError(f"snum format issue: {s=}")

        if leaf != "R" and leaf != "L" and leaf is not None:
            raise TypeError(f"leaf issue: {leaf=}")

        if type(s[0]) is list:
            self.left = Snum(s[0],"L",self)
        elif type(s[0]) is int:
            self.left = s[0]
        elif type(s[0]) is Snum:
            self.left = s[0]
            self.left.leaf = "L"
        else:
            raise TypeError(f"Left element issue: {s[0]=}")

        if type(s[1]) is list:
            self.right = Snum(s[1],"R",self)
        elif type(s[1]) is int:
            self.right = s[1]
        elif type(s[1]) is Snum:
            self.right = s[1]
            self.right.leaf = "R"
        else:
            raise TypeError(f"Right element issue: {s[1]=}")

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def mag(self):
        if type(self.left) is Snum:
            mag = 3*self.left.mag()
        else:
            mag = 3*self.left
        if type(self.right) is Snum:
            return mag + 2*self.right.mag()
        else:
            return mag + 2*self.right

    def depth(self):
        d = 1
        n = self
        while n.parent is not None:
            n = n.parent
            d += 1
        return d

    def reduce(self):
        changed = True
        while changed:
            print(self)
            while changed:
                changed = self.explode()
                print(self)
            changed = self.split()

    def explode(self):
        if self.depth() > 4:
            print(f"exploding {self=}")
            if type(self.left) is Snum or type(self.right) is Snum:
                raise TypeError(f"TOO DEEP: {Snum.left, Snum.right}")
            l, r = self.left, self.right
            if self.leaf == "L":
                n = self.parent
                m = self.parent
                n.left = 0
                #add the right value to leftmost leaf
                if type(n.right) is int:
                    n.right += r
                else:
                    n = n.right
                    while type(n.left) is not int:
                        n = n.left
                    n.left += r
                #add the left value to rightmost leaf
                pass
                while m is not None and m.leaf != "R":
                    m = m.parent
                if m is not None:
                    if type(m.left) is int:
                        m.left += l
                    else:
                        while type(m.right) is Snum:
                            m = m.right
                        m.right += l

            elif self.leaf == "R":
                n = self.parent
                m = self.parent
                n.right = 0
                #add the left value to rightmost leaf
                if type(n.left) is int:
                    n.left += l
                else:
                    n = n.left
                    while type(n.right) is not int:
                        n = n.right
                    n.right += l
                #add the right value to leftmost leaf
                pass
                while m is not None and m.leaf != "L":
                    m = m.parent
                if m is not None:
                    if type(m.right) is int:
                        m.right += r
                    else:
                        while type(m.left) is Snum:
                            m = m.left
                        m.left += r

            else:
                raise TypeError(f"invalid leaf: {self.leaf=}")
            return True

        if type(self.left) is Snum:
            if self.left.explode():
                return True

        if type(self.right) is Snum:
            if self.right.explode():
                return True

        return False

    def split(self):
        if type(self.left) is Snum:
            if self.left.split():
                return True
        elif type(self.left) is int and self.left > 9:
            print(f"splitting left {self=}")
            self.left = Snum([floor(self.left/2),ceil(self.left/2)], "L", self)
            return True

        if type(self.right) is Snum:
            if self.right.split():
                return True
        elif type(self.right) is int and self.right > 9:
            print(f"splitting right {self=}")
            self.right = Snum([floor(self.right/2),ceil(self.right/2)], "R", self)
            return True

        return False

    def __add__(self, other):
        if type(other) is not Snum:
            raise TypeError(f"Can not add {type(other)} to Snum")
        s = Snum([self,other],None,None)
        self.parent = s
        self.leaf = "L"
        s.right.parent = s
        s.right.leaf = "R"
        s.reduce()
        return s

    def copy(self):
        pass

def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.strip())
    return data

if __name__ == "__main__":
    data = load_data("18.data")
    data = [ "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]", "[[[5,[2,8]],4],[5,[[9,9],0]]]", "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]", "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]", "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]", "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]", "[[[[5,4],[7,7]],8],[[8,3],8]]", "[[9,3],[[9,9],[6,[4,9]]]]", "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]", "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]", ]
    data = [ "[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]" ]

    numbers = []
    for line in data:
        numbers.append(Snum(json.loads(line),None,None))

    s = numbers[0]
    for n in numbers[1:]:
        s += n
        
    print(s, s.mag())
