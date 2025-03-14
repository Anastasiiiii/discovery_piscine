#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else: 
    for i in parameters:
        if not i.endswith("ism"):
            i = i + "ism"
            print(i)
