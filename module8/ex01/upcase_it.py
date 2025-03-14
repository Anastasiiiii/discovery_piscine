#!/usr/bin/env python3

def upcase_it(my_string):
    try:
        my_string = my_string.upper()
        return my_string
    except AttributeError:
        return "Input is not a string"
    except TypeError as e:
        return str(e)

print(upcase_it("hello"))
print(upcase_it(42))
