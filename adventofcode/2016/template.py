#!/usr/bin/env python3

"""
"""

def load_data(filename: str) -> list:
    data = []
    with open(filename, "r") as f:
        for line in f:
            data.append(line.rstrip())
    return data

if __name__ == "__main__":
    data = load_data("CHANGEME.data")
    data = load_data("CHANGEME.test")
