# create a program that reads 2 values and shows a menu on screen:
# [1] sum [2] multiply [3] biggest [4] new numbers [5] exit program

from time import sleep

print('\033[1;36m=====Calculator=====\033[m')

print("""\033[m[ 1 ] sum
[ 2 ] multiply
[ 3 ] show greatest number
[ 4 ] new numbers
[ 5 ] exit program """)

option = 0

while option != 5 or option == 4:

    n1 = int(input('\nFirst number: '))
    n2 = int(input('Second number: '))

    option = int(input('\n>>>>>What would you like to do? '))

    if option == 1:
        print('{} + {} ='.format(n1, n2), n1 + n2)
    elif option == 2:
        print('{} * {} ='.format(n1, n2), n1 * n2)
    elif option == 3:
        print('The greatest number is:', end=' ')
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    else:
        print('Invalid option. Try again please.')
    sleep(1.5)

print('\nThank you for using calculator.')
