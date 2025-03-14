#!/usr/bin/env python3
import sys
import re

parameters = sys.argv[1:]
if len(parameters) != 2:
    print("none")
else:
    matches = re.findall(parameters[0], parameters[1])
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))
