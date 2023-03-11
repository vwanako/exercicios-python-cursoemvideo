# the same teacher from before wants to randomly pick the order that the students will present their assignments

from random import shuffle

student_1 = input("First student:")
student_2 = input("Second student: ")
student_3 = input("Third student: ")
student_4 = input("Fourth student: ")

name_list = [student_1, student_2, student_3, student_4]

shuffle(name_list)

print("The order of the presentations is: {}".format(name_list))

