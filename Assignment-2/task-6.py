"""
Task 6. (Double points!)
A prime number is a number that has exactly two natural number (number > 0) divisors: one
and the number itself. Thus, the ten smallest prime numbers are 1, 2, 3, 5, 7, 11, 13, 17, 19 and
23 as any of the cannot be evenly divided by other numbers than one and the number itself.
Write a program that queries the user for a number and proceeds to output whether the number
is a prime number or not. Example run:
Enter a number: 43
43 is a prime number
Another example run:
Enter a number: 22
22 is not a prime number
"""
num = int(input("Enter a number: "))
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")