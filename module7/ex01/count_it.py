#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]
if len(parameters) == 0:
    print("none")
else:
    print(f"parameters: {len(parameters)}")
    for i in parameters:
        print(i + ":", len(i))
