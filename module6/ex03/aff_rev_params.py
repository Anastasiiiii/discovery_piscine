#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]
if len(parameters) < 2:
    print("none")
else:
    i = len(parameters) - 1
    while i >= 0:
        print(parameters[i])
        i -= 1
