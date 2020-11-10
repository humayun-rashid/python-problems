"""
Write a function combine(d1,d2) that combines two dictionaries. Combining is done by adding
values from d2 to d1. Naturally this means that if there are same values, they will be overwritten.
Example run (in python Shell):
d1 = {"a" : 4, "b" : 5}
d2 = {"b" : 8, "c" : 10}
combine(d1,d2)
print(d1)
{"a": 4, "b": 8, "c": 10}
"""

def combine(dict1, dict2):
    return(dict1.update(dict2))


d1 = {"a" : 4, "b" : 5}
d2 = {"b" : 8, "c" : 10}
combine(d1,d2)
print(d1)