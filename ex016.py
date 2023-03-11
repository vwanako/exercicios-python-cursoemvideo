# create a program that reads any real number and displays its whole part

from math import trunc

number = float(input("Type a random real number and I will display the its whole part: "))
whole_part = trunc(number)

print("The whole part of {} is {}.".format(number, whole_part))
