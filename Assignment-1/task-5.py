"""
Task 5.
Write a program that queries the user for a string containing a DNA sequence, and proceeds
to output the proportions of four nucleotide bases (A, C, G and T) as percentage values. You
can assume that the user enters the sequence in lower case. If the user enters an empty string,
display an error message.
Example run:
Enter sequence: aaaagctgcggta
Proportion of A: 38 percent
Proportion of T: 15 percent
Proportion of C: 15 percent
Proportion of G: 30 percent
Display the numbers either in Integers (and observe that the example has an inevitable rounding
error) or display the numbers with decimals.
"""

stringInput= str(input("Enter sequence:"))
stringInput = stringInput.lower()
sequenceLength= int(len(stringInput))

A = (int(stringInput.count("a"))/sequenceLength)*100
print("Proportion of A:",A ,"percent")

T = (int(stringInput.count("t"))/sequenceLength)*100
print("Proportion of T:",T ,"percent")

C = (int(stringInput.count("c"))/sequenceLength)*100
print("Proportion of A:",C ,"percent")

G = (int(stringInput.count("g"))/sequenceLength)*100
print("Proportion of G:",G ,"percent")

