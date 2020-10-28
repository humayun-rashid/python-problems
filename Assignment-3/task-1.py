"""
Enter a number or a zero to quit: 3
Enter a number or a zero to quit: 7
Enter a number or a zero to quit: 1
Enter a number or a zero to quit: 0
List: [1, 3, 7]
"""
number_list= list()

while True:
    number = int(input("Enter a number or a zero to quit:"))
    if number ==0:
        break
    else:
        number_list.append(number)

number_list.sort()
print(number_list)
