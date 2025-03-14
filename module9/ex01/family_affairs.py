#!/usr/bin/env python3

#A function to find all red-head family members
def find_the_redheads(data: dict):
    try:
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError("All keys and values must be strings")
        #filter to find a string "red"    
        results = list(filter(lambda key: data[key] == "red", data))
        if len(results) < 1:
            return None 
        return results
    except AttributeError:
        return "Input is not a dictionary"
    except TypeError as e:
        return str(e)


#A data set with red-head family member
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))

#A data set with no read-head family member
birds_family = {
    "florian": "black",
    "marie": "blond",
    "virginie": "brunette",
    "david": "black",
    "franck": "black"
}

print(find_the_redheads(birds_family))

#A data set with no string values
number_family = {
    "florian": 5,
    "marie": "blond",
    "virginie": "brunette",
    "david": "black",
    "franck": "black"
}

print(find_the_redheads(number_family))
