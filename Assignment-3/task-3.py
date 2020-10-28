"""
Task 3.
Write a function min_max(my_list) which returns the minimum and maximum of the values
stored in the list my_list. You can either return two values with syntax
return a, b
OR create a list with the two items and return the list.
Example run (in Python Shell):
 n = [1,5,3,1,4,2,3]
 mn, mx = min_max(n)
 print("min and max: ", mn, mx)
min and max: 1 5
or
 n = [1,5,3,1,4,2,3]
 values = min_max(n)
 print("min and max: ",values)
min and max: [1, 5]
"""
def min_max(my_list):
    a = min(my_list)
    b = max(my_list)
    return a,b
    
n = [1,5,3,1,4,2,3]
mn, mx = min_max(n)
print("min and max: ", mn, mx)




