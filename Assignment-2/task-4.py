"""
Task 4.
Write a program that queries the user for a string, and proceeds to generate a new string with
all of the letters from the original string that are in upper case. This generated string is then
output. You can assume that the string given does not contain characters other than letters (e.g.
numbers or spaces).
Example run:
Enter a string: AbcDeFgYTkm
Characters in upper case: ADFYT
"""
string = str(input("Enter a string: "))
new_string=""
for char in string:
    if char.isupper() == True:
        new_string = new_string + char
print(new_string)

    
    