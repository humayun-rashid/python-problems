"""
Task 1.
Use method randint from module random to write a program, that queries the user for a number,
then proceeds to generate that many random numbers between 1 and 100 and store them into a
list. Finally output the list.
Example run:
Enter a number: 5
[11, 32, 4, 91, 6]
"""
import random
random_list = []
user_input = int(input('Enter a number:'))
for n in range(user_input):
    random_number=(random.randint(1,100))
    random_list.append(random_number)
print(random_list)