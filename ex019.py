# a teacher wants to randomly pick one of his four students to erase the board.
# make a program that reads their names and displays the chosen one.

import random

name_input = input("Write the name of the students, separated by a space: ")
name_list = name_input.split(" ")
student_chosen = random.choice(name_list)

print("The chosen student is {}".format(student_chosen))
