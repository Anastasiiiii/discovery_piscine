#!/usr/bin/env python3

def add_one(number: int) -> int:
    try:
        number += 1
        return number
    except TypeError as e:
        return str(e)

number = 5
second_number = 42
print(add_one(number))
print(add_one(second_number))
