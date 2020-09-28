
#Give the 1st string: hello
#Give the 2nd string: hey
#hello is longer.

#Take two input
first_input = str(input("Give first string: "))
second_input = str(input("Give second string: "))

#Get the length of the input
first_input_len = len(first_input)
second_input_len = len(second_input)

#Print the bigger one with if-else condition
if first_input_len > second_input_len:
    print(first_input,"is longer")

if first_input_len < second_input_len:
    print(second_input,"in longer")

if first_input_len == second_input_len:
    print("Both are same size")