# make a program that reads someone's gender, but only accept the values 'M' or 'F'. Repeat the question if the value !=

gender = input('What is your gender? (M/F): ')

while gender not in 'MmFf':
    gender = input('Invalid data. Please choose one of the options(M/F): ')

print('Data has been registered, thank you.')
