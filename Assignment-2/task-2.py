"""
Task 2.
Write a program that queries the user for number, and proceeds to output whether the number
is an even or an odd number. Program keeps asking more and more numbers and terminates,
when the user enters a zero.
Example run:
Enter a number or a zero to quit: 8
That’s an even number
Enter a number or a zero to quit: 13
That’s an odd number
Enter a number or a zero to quit: 0
Bye!
"""
integerNumber = int(input("Enter a number or a zero to quit:"))

while integerNumber != 0:
    if (integerNumber%2) == 0:
        print("That’s an even number")
    else:
        print("That’s an odd number")
        
    integerNumber = int(input("Enter a number or a zero to quit:"))

