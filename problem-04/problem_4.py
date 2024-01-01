# Write a Python program to get the smallest number from a list.

# SOLUTION - 1
list4 = [10,25,36,44,78,3.25,64,23]
print(f'The smallest number is {min(list4)}')

# OR

# SOLUTION - 2
list4 = []
num_elements = int(input('Enter the number of elements: '))
for i in range(num_elements):
  element = float(input(f'Enter the {i+1} element: '))
  list4.append(element)

print(f'The smallest number in the list is {min(list4)}')
