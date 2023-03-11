# Make a program that reads 5 numeric values and stores them in a list. In the end, show the biggest and smallest values
# as well as the position they were in.

numbers = list()

for n in range(0, 5):
    numbers.append(int(input('Type a number: ')))
