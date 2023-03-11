# Make a multiplication table using for loops

print('\033[34m-+-' * 7)
print('\033[1;34mmultiplication table')
print('\033[34m-+-' * 7)

number = int(input('\033[mType a number: '))

print('-' * 11)
for i in range(1, 11):
    print('{} x {} = {}'.format(number, i, number * i))
print('-' * 11)
