# Create a program that generates 5 random numbers and put them in a Tuple. Then show a list of the numbers and what are
# the smallest and biggest values.

from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'The numbers were {numbers}')

print(f'The biggest number is {max(numbers)}')
print(f'The smallest number is {min(numbers)}')
