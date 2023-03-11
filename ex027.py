# Make a program that reads name and splits it between first and last name

name = input("What is your name? ").strip().split(' ')

print("Your first name is {}".format(name[0]))
print("Your last name is {}".format(name[-1]))
