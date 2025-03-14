#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: ", numbers)
numbers_set = set()
new_numbers = []

for i in numbers:
    if i > 5 and i not in numbers_set:
        numbers_set.add(i)
        number = i + 2
        new_numbers.append(number) 

print("New array: ", new_numbers)
