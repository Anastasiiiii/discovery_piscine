#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

#Delete characters till len is 8
def shrink(arg = None):
    try:
        if arg is None:
            print("There is should be an argument")
        while len(arg) > 8:
            arg = arg[:-1]
        return arg
    except AttributeError:
        return "Input is not a string"
        

#Add Z character till len is 8
def enlarge(arg = None):
    try:
        if arg is None:
            print("There is should be an argument")
        while len(arg) < 8:
            arg += 'Z'
        return arg
    except AttributeError:
        return "Input is not a string"


if len(parameters) < 1:
    print("none")
else:
    for parameter in parameters:
        if len(parameter) > 8:
            print(shrink(parameter))
        elif len(parameter) < 8:
            print(enlarge(parameter))
        else:
            print(parameter)
