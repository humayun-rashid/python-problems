"""
Task 6. (Double points!)
Write a program that queries a number. The problem is that you don’t know what kind of
number it is.
User might enter any of the following:
123 # a valid Integer
156.23 # a valid float
5.22.3 # invalid float (too many points)
abcd # not a number
Your task is to:
1. Check if the value is a valid number
2. If it is, convert it to the proper type (int or float by using the function)
3. Print the type
4. Otherwise print what the problem was
Example run:
Give a number: 123
This is int
Example run:
Give a number: 420.69
This is float
Example run:
Give a number: 1.22.34
Not a number (too many points)
Example run:
Give a number: abcd
Not a number (contains other than numbers)
Whether or not the string is a number, can be tested with the function my_string.isdecimal().
The function only returns True, if there are only digits 0-9. This does not count the dots, so you
might have to replace the dots first with something before using the functions.
Hint: The string is a number, if it has only decimal characters (0-9) and maximum of one dot.
Hint: Figure out all the properties first: is there only numbers? how many dots? Then use
previous lectures information to solve this.
Note: Exception handling is not needed, as it has not been covered yet
"""

userNumber= input("Give a number:")
checkString = any(map(str.isalpha, userNumber))
checkDecimal=any(map(str.isdecimal, userNumber))
checkDigit = any(map(str.isdigit, userNumber))

if "." not in userNumber and checkString==False and (checkDecimal and checkDigit)==True:
    convertInt = int(userNumber)
    print("a valid Integer")

if "." in userNumber and checkString==False and (checkDecimal and checkDigit)==True:
    dotAmount = userNumber.count(".")
    if dotAmount > 1:
        print("Not a number (too many points)")
    if dotAmount == 1:
        convertFloat = float(userNumber)
        print("a valid float")

if  (checkString==True and checkDecimal==False and checkDigit==False) or ("." in userNumber and checkString==True and checkDecimal==True and checkDigit==True):
    print("Not a number (contains other than numbers)")
