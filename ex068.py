# Create a program that plays even or odd with the computer. The program will stop when the player loses. Show how many
# consecutive wins the player got.

from random import randint

computer = user = win = 0
green = '\033[1;32m'
red = '\033[1;31m'
normal = '\033[m'

while True:
    user = int(input(f'{normal}Type a number from 0 to 10: '))
    computer = randint(0, 10)
    even_or_odd = str(input('Even or odd [E/O]? '))

    soma = computer + user

    print(f'\nYou picked {green}{user}{normal}, the computer picked {red}{computer}{normal}, the total is {soma}.')

    if soma % 2 == 0 and even_or_odd in 'Ee':
        print(f'\n{green}You win! Keep going.{normal}')
        win += 1

    elif soma % 2 != 0 and even_or_odd in 'Oo':
        print(f'\n{green}You win! Keep going.{normal}')
        win += 1

    else:
        print(f'\n{red}You lose!{normal}')
        break

print('=' * 25)
print(f'You beat me {green}{win}{normal} time(s)!')
