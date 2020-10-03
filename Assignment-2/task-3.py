"""
Write a program that queries the user for a number N, and then proceeds to output all powers
of two smaller than N.
For example, if N is given a value 9, numbers 1, 2, 4 and 8 are output 
Example run:
Enter a number: 21
1
2
4
8
16
"""
number = int(input("Enter a number: "))
for a in range (number):
    result=2**a
    if result < number:    
        print(result)
   