# Make a program that reads a whole number and shows the number before, and the number after itself

number = int(input("Pick a number and I will show you the number before and after it. "))


print("The number before {} is {} and the number after {} is {}".format(number, number + 1, number, number - 1))
