# Develop a program that reads two grades from a student, calculates and shows their average

name = (input("Hello user! Tell me your name, please :) "))

print("Welcome, {}, I'm GradeBuddy. I'll calculate your two last grades' average. Type them below please.".format(name))

grade_1 = float(input("First grade: "))
grade_2 = float(input("Second grade: "))
average = (grade_1 + grade_2)/2

print("Your grades were {} and {}, correct? So your average is {:.2f}!".format(grade_1, grade_2, average))

if average >= 6:
    print("Congratulations {}, you passed!".format(name))
elif average < 6:
    print("You didn't pass, {} :(. You'll have to try harder.".format(name))
