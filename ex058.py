# re-do challenge 28, where the computer will think of a number between 0 and 10. Now it repeats until the user guesses
# right, showing how many guesses were necessary to win

from random import randint

print('NUMBER GUESSING GAME')
computer = randint(0, 10)
user = int(input('I thought of a number between 0 and 10, try to guess it: '))
guesses = 1

while user != computer:
    print('Nope, it was not {}.'.format(user))
    guesses += 1
    if computer > user:
        user = int(input('It is bigger than {}: '.format(user)))
    else:
        user = int(input('It is smaller than {}: '.format(user)))

print('Yes, {} is correct! It took you {} guesses to get it right.'.format(computer, guesses))
