#!/usr/bin/env python3

input_number = int(input("Enter a number: \n"))
multiplier_number = 0

print("The multiplication table:")
while multiplier_number  <= 9:
    result = multiplier_number * input_number
    print(f"{multiplier_number} x {input_number} = {result}")
    multiplier_number += 1
