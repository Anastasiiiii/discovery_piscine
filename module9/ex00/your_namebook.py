#!/usr/bin/env python3

#To put names wih capitalized first letter into the array
def array_of_names(data: dict):
    try:
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError("All keys and values must be strings")
        #Making capitalized names array
        names_array = [f"{key.capitalize()} {value.capitalize()}" for key, value in data.items()]
        return names_array
    except AttributeError:
        return "Input is not a dictionary"
    except TypeError as e:
        return str(e)

#A dictionary for the example
persons = {
    "jean": "beautiful",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

persons2 = {
    "jean": 5,
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons2))
