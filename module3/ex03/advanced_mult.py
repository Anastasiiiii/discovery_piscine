#!/usr/bin/env python3

for i in range(0, 11):
    print(f"Table of {i} : ", end = " ")
    for j in range(0, 11):
        result = i * j
        print(result, end = " ")
    print()
