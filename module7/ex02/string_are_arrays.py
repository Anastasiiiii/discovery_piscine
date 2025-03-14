#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

if len(parameters) != 1 or 'z' not in parameters[0]:
    print("none")
else:
    print(end = " ")
    for i in parameters[0]:
        if i == 'z':
            print('z', end = " ")
    print()

