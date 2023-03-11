# Make a program that reads a whole number and says if it's primo or not

num = int(input('Number: '))

# amount of times the number was divisible
tot_div = 0

for i in range(1, num + 1):

    # everytime it is divisible by a number, we will display the number and add 1 to tot_div
    if num % i == 0:
        print('\033[1;32m', end=' ')
        tot_div += 1

    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')

# a number is primo if it can be ONLY be divided by 1 and itself, so tot_div == 2
if tot_div == 2:
    print('\nThe number is primo.')

elif tot_div > 2:
    print('\n\033[31mThe number is not primo.')
