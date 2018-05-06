#!/usr/bin/env python
import argparse
import importlib
import sys


def run(day, part, input):
    try:
        module = importlib.import_module("aoc{}".format(day))
        fn = getattr(module, "aoc{}_{}".format(day, part))
        print(fn(input))
    except ModuleNotFoundError as e:
        print("Puzzle does not exist or is not yet implemented")
        sys.exit(1)
    except AttributeError as e:
        print("Puzzle has no such part or it is not yet implemented")
        sys.exit(1)


if __name__ == "__main__" and __package__ is None:
    parser = argparse.ArgumentParser()
    parser.add_argument("day")
    parser.add_argument("part")
    args = parser.parse_args()
    run(args.day, args.part, sys.stdin.read().rstrip())
