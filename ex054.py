# Create a program that reads the year of birth of seven people. In the end, show how many of those people are over 18
# And how many aren't

from datetime import date

over_18 = 0
under_18 = 0

for i in range(1, 8):
    yob = int(input('Year of birth {}: '.format(i)))
    age = date.today().year - yob
    if age >= 18:
        over_18 += 1
    else:
        under_18 += 1

print("""There are \033[1;34m{}\033[m people \033[1;34m18 or over\033[m
and also \033[1;32m{}\033[m people \033[1;32munder 18\033[m.""".format(over_18, under_18))
