"""
Write a procedure remove_duplicates(n), which finds and removes duplicate items from a list
given as an argument. Hence, after the procedure is called, only a single instance of each item
can be found in a list.
 lst = [1, 2, 1, 3, 3, 2, -1, 5, 3, 5, -1, 2, 5]
 remove_duplicates(lst)
 print (lst)
[1, 2, 3, -1, 5]
"""
def duplicate_remover(x):
    # Convert to dictionary from list
    dict_from_list = dict.fromkeys(x)
    list_from_dict = list(dict_from_list)
    
    return list_from_dict

lst = [1, 2, 1, 3, 3, 2, -1, 5, 3, 5, -1, 2, 5]

mylist = duplicate_remover(lst)

print(mylist)
