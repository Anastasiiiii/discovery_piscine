#!/usr/bin/env python3
import statistics

#A function to find an average mark in the class
def average(data: dict):
    try:
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, int):
                raise TypeError("All keys must be strings and all values must be integers")
        #Finding averege mark
        marks = [value for value in data.values()]
        average_mark = statistics.mean(marks)

        return average_mark
    except AttributeError:
        return "Input is not a dictionary"
    except TypeError as e:
        return str(e)


#A data set for an example
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

class_3D = {
    "quentin":  "17",
    5: 15,
    "marc": 8,
    "stephanie": 13
} 
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
print(f"Average for class 3C: {average(class_3D)}.")
