"""
Write a program that queries the user for two strings, and proceeds to test and output whether
the first string contains all letters of the second string in reverse order.
Example run:
Give the 1st string: abcd
Give the 2nd string: dcba
abcd IS dcba in reverse order!
Another:
Give the 1st string: testing
Give the 2nd string: hello
abcd IS NOT hello in reverse order!
Hint: Check the ”trick” about reversing a string from the previous weeks material about string
slicing.
"""

#Get the length of the input
firstString = str(input("Give the 1st string: "))
secondString = str(input("Give the 2nd string: "))

firstStringLength=len(firstString) # calculate length of the list
reverseString=firstString[firstStringLength::-1] # slicing that will reverse the value of first string 
print(reverseString)
# Check if the second string is reverse of the first string

if secondString == reverseString:
    print(firstString, "IS", secondString, "in reverse order!")
else:
    print(firstString, "IS NOT",secondString , "in reverse order!")

