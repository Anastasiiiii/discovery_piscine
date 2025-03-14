#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]
if len(parameters) != 1:
    print("none")
else:
    result = parameters[0].lower()
    print(result)
