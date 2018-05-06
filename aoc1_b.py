#!/usr/bin/env python
import argparse


def aoc1_b(input):
    total = 0
    n_items = len(input)
    halfway_offset = int(n_items / 2)
    for x in range(n_items):
        this = int(input[x])
        halfway_item = int(input[(x + halfway_offset) % n_items])

        if this == halfway_item:
            total += this

    return total


if __name__ == "__main__" and __package__ is None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()
    print(aoc1_b(args.input))
