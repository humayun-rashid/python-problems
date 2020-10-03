"""
Task 1.
Write a program that queries the user for a number N, and then proceeds to output all numbers
between -N and N.
Example output: Enter a number: 3
-3
-2
-1
0
1
2
3
"""
n = int(input("Enter a number: "))

for i in range (0-n,0+n+1,1):
    print i