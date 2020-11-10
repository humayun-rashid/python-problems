"""
Write a function dictToList(d), which gets a dictionary as an argument. The function creates
a new list containing all keys and values from the dictionary as tuples. Each tuple consists of a
key and the corresponding value (in that order). Finally, the generated list is returned.
Example run (in Python Shell):
 dict = {0 : "abc", 2 : "bcd", 3: "cde", 4 : "def"}

[(0, "abc"), (2, "bcd"), (3, "cde"), ( 4, "def")]
"""

def dict_to_list(dict):
    result = list(zip(dict.keys(), dict.values()))
    return result
dict = {'Mon': '2 pm', 'Tue': '1 pm', 'Fri': '3 pm'}
myList = dict_to_list(dict)
print (myList)