# Create a program that reads age and gender of multiple people. Ask the user if they want to continue typing or not.
# Show: a) how many people over 18 b) how many men were registered c) how many women are under 20.
# Include a valid result feature. Don't accept invalid answer.

over18 = wu20 = men = 0

while True:
    gender = str(input('\nGender [M/F]: '))
    while gender not in 'MmFf':
        gender = str(input(f'{gender} is not a valid option. Gender [M/F]: '))
    age = int(input('Age: '))

    if age >= 18:
        over18 += 1
    if gender in 'Ff' and age <= 20:
        wu20 += 1
    if gender in 'Mm':
        men += 1

    user = str(input('Continue [Y/N]? '))
    while user not in 'YyNn':
        user = str(input(f'{user} is not a valid option. Continue [Y/N]? '))
    if user in 'Nn':
        break

print('\nDone!')
print(f'I registered {over18} people over 18, {men} men and {wu20} women under 20.')
