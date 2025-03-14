#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

try:
    if len(parameters) != 2:
        print("none")
    else:
        array = [i for i in range(int(parameters[0]), int(parameters[1]) + 1)]
        print(array)
except ValueError:
    print("Input must be integers")
