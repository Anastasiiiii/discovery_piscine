#!/usr/bin/env python3

user_age = int(input("Please tell me your age: "))
print(f"You are currently {user_age} years old.")

in_years = 10
while in_years <= 30:
    future_age = user_age + in_years
    print(f"In {in_years} years, you'll be {future_age} years old.")
    in_years += 10
