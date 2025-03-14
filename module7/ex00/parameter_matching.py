#!/usr/bin/env python3
import sys

input_parameter = input("What was the parameter? ").strip()

parameters = sys.argv[1:]
if len(parameters) != 1:
    print("none")
elif input_parameter == parameters[0]:
    print("Good job!")
else:
    print("Nope, sorry...")
