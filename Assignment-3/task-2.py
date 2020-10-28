"""
Write a function average(m), which calculates and returns the average of all items in the list m
Example run (in Python Shell):
my_list = [2,4,6,8,11]
average(my_list)
6.2
"""
def avg(my_list):
  avg = sum(my_list)/len(my_list)
  print(avg)
  return avg

my_list = [2,4,6,8,11]
avg(my_list)