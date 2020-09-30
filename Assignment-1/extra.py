"""
Program generates three random numbers and stores them into three variables, n1, n2 and n3. 
Finish the program by outputting the middle one of the numbers. 
For example, if the values are 11, 22 an 7, you should output 11. 
Do not  not output anything else but the number!
"""
# Import random library
import random

# generate 3 random number to n1,n2,n3
n1 = random.randint(0,1000) 
n2 = random.randint(0,1000)
n3 = random.randint(0,1000)
#Print random numers
print(n1,n2,n3)
# Get middle number and print only the number
if n1>n2 and n1<n3:
    middleNumber = n1
    print(middleNumber)

elif n2>n1 and n2<n3:
    middleNumber = n2
    print(middleNumber)

elif n3>n1 and n3<n2:
    middleNumber = n3
    print(middleNumber)
