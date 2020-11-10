"""
Task 2.
Write a program that queries the user for persons’ names and ages and saves them into a dictionary with name as a key and age as a value. When the user enters an empty string as a name,
the program outputs the dictionary and terminates.
Example run:
Enter a name or an empty string to stop: James
Enter age: 25
Enter a name or an empty string to stop: Jane
Enter age: 31
Enter a name or an empty string to stop:
{'James' : 25, 'Jane' : 31 }
"""
user_dict = {}
while True:
    name = str(input('Enter a name or an empty string to stop:'))
    if name == "":
        print(user_dict)
        break
    else:
        age = str(input('Enter age:'))
        user_dict[name] = age

