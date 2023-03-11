# Make a program that reads a random year and says if it is a leap year

from datetime import date

year = int(input('What year do you want to analise? Type 0 to analise current year: '))

if year == 0:
    year = date.today().year

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("The year {} is a leap year.".format(year))

else:
    print("The year {} is not a leap year.".format(year))
