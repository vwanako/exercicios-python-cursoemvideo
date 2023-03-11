# Make a program that reads an athletes date of birth and shows their age category:
# <=9yo: sub-9 <=14yo: sub-14 <=19yo: junior <=25: senior above that: master

from datetime import date

yob = int(input("Inform athlete's year of birth: "))
age = date.today().year - yob

print('Athlete is {} years old.'.format(age))

if age <= 9:
    print('Age category: Sub-9'.format(age))

elif age <= 14:
    print('Age category: Sub-14'.format(age))

elif age <= 19:
    print('Age category: Junior'.format(age))

elif age <= 25:
    print('Age category: Senior'.format(age))

else:
    print('Age category: Master'.format(age))
