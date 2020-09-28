"""
Give the 1st string: hello
Give the 2nd string: hey
hello is longer.
"""

#Take two input
firstString = str(input("Give the 1st string:"))
secondString = str(input("Give the 2nd string:"))

#Get the length of the input
firstStringLength = len(firstString)
secondStringLength = len(secondString)

#Print the bigger one with if-else condition
if firstStringLength > secondStringLength :
    print(firstString,"is longer")

if firstStringLength< secondStringLength:
    print(secondString,"in longer")

if firstStringLength == secondStringLength:
    print("Both are same size")