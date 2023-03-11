# Create a program that reads a random whole number and say if it is even or odd

number = int(input('Please type a whole number: '))

if (number % 2) == 0:
    print("The number {} is even.".format(number))
else:
    print("The number {} is odd".format(number))
