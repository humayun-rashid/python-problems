"""
Write a function unique_items(list1, list2), which gets two lists as an argument, and returns
a new list that contains all unique items from both lists. Utilize sets to create the list.
Example run(in Python Shell):
l1= [1,2,1,3]
l2 = [2,3,4,5]
l3 = unique_items(l1,l2)
print (l3)
[1, 2, 3, 4, 5]
"""

def unique_items(l1,l2):
    l3 = []
    for element in l1:
        if element not in l3:
            l3.append(element)
    for element in l2:
        if element not in l3:
            l3.append(element)
    return l3

l1= [1,2,1,3]
l2 = [2,3,4,5]

l3 = unique_items(l1,l2)
print (l3)
    