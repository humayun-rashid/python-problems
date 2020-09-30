"""
Task 3.
Write a program that queries the user for three numbers and outputs the smallest of them.
Example run:
Give the first number: 11
Give the second number: 4
Give the last number: 7
Smallest number is: 4
Make sure it works with all the following numbers (given in this order, one line per program
run):
1,2,3
3,2,1
1,3,2
Also:
3,3,2
3,2,3
2,3,3
If you succesfully get the smallest output in all these six cases, you most likely get any other
arrangement correct as well.
If you feel like it, test with these remaining cases as well:
2,3,1
2,1,3
3,1,2
"""
# queries the user for three numbers
firstNumber = int(input("Give the first number: "))
secondNumber = int(input("Give the second number: "))
thirdNumber = int(input("Give the third number: "))

# Check shortest number and print
if firstNumber < ( secondNumber and thirdNumber):
    smallestNumber = firstNumber
    print("smallest number is", smallestNumber)

if secondNumber < ( firstNumber and thirdNumber):
    smallestNumber = secondNumber
    print("smallest number is", smallestNumber)

if thirdNumber < ( secondNumber and firstNumber):
    smallestNumber = thirdNumber
    print("smallest number is", smallestNumber)