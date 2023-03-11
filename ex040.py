# Write a program that reads a student's grade and displays a message saying:
# Approved if the grade is above 7.0, summer school if the grade is between 5.0 and 6.9, and failed if < 5.0

grade_1 = float(input('Grade 1: '))
grade_2 = float(input('Grade 2: '))
grade = (grade_1 + grade_2) / 2

print('You final grade was {}.'.format(grade))

if grade >= 7.0:
    print("\033[1;32mStudent approved! Congratulations!!")
elif 6.9 >= grade >= 5.0:
    print("\033[1;33mSummer school. You still have a chance!")
else:
    print("\033[1;31mFailed. Your grade was way below average, study harder.")
