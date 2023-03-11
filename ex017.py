# create a program that reads the sizes of the cathetus in a right triangle and calculates the size of the hypotenuse

from math import hypot

cat_1 = float(input("What is the size of the first cathetus? "))
cat_2 = float(input("What is the size of the secont cathetus? "))
hypotenuse = hypot(cat_1, cat_2)

print("The hypotenuse of {} and {} is {:.2f}".format(cat_1, cat_2, hypotenuse))

