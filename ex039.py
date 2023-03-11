# Write a program that reads the date of birth of a man and says, according to his age, if:
# He will still need to sign up for the military, if it is time to sign up or if the time to sign up has passed
# Your program should also show the time remaining or that passed the due date

from datetime import date

dob = int(input('Year of birth: '))
current_year = date.today().year
age = current_year - dob

print('You are {} years old in {}'.format(age, current_year))

if age < 18:
    print("You're not old enough to go to the military yet.")
    print("You will have to go to the military in {} years.".format(18 - age))
elif age == 18:
    print("It's time for you to go to the military.")
elif age > 18:
    print("Your time to go to the military has passed.")
    print("It has been {} years since you were supposed to go.".format(age - 18))
