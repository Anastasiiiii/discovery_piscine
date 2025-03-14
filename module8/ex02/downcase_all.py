#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

def downcase_it(my_string):
    try:
        my_string = my_string.lower()
        return my_string
    except AttributeError:
        return "Input is not a string"
    except TypeError as e:
        return str(e)

if len(parameters) < 1:
    print("none")
else:
    for parameter in parameters:
        print(downcase_it(parameter))
