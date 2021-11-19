#!/usr/bin/env pypy3

"""
"""

def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            pass
    return data

if __name__ == "__main__":
    data = load_data("01.data")
