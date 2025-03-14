#!/usr/bin/env python3

first_number = float(input("Give me the first number: "))
second_number = float(input("Give me the second number: "))
print("thank you!")

#Adding
result = first_number + second_number
print(f"{first_number} + {second_number} = {round(result, 2)}")

#Subtracting
result = first_number - second_number
print(f"{first_number} - {second_number} = {round(result, 2)}")

#Dividing
if second_number == 0:
    print("Error! You cannot divide by zero!")
else: 
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {round(result, 2)}")

#Multiplying
result = first_number * second_number
print(f"{first_number} x {second_number} = {round(result, 2)}")
