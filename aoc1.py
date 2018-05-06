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
