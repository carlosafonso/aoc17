#!/usr/bin/env python
import argparse


def aoc1_a(input):
    total = 0
    for x in range(len(input)):
        this = int(input[x])
        if x == len(input) - 1:
            next = int(input[0])
        else:
            next = int(input[x + 1])

        if this == next:
            total += this

    return total


if __name__ == "__main__" and __package__ is None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()
    print(aoc1_a(args.input))
