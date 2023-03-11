# Create a program that plays Rock, Paper, Scissors with you.

from random import choice
from time import sleep

print('\033[35m-+-\033[m' * 12)
print("\033[1;35mlet's play rock, paper, scissors!!\033[m")
print('\033[35m-+-\033[m' * 12)

plays = ['rock', 'paper', 'scissors']

user = input('Your move: ').strip().lower()
computer = choice(plays)

print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Po!')
sleep(0.5)

print('-=-' * 5)
print('I chose {}{}{}, \nyou chose {}{}{}'.format('\033[1;31m', computer, '\033[m', '\033[1;32m', user, '\033[m'))
print('-=-' * 5)

sleep(0.5)

if user == computer:
    print("\033[1;36mIt's a tie!")

elif user != computer:
    # User wins:
    if ((user == plays[0]) and (computer == plays[2])) or ((user == plays[1]) and (computer == plays[0])) or ((user == plays[2]) and (computer == plays[1])):
        print('\033[1;32mYou win!!')

    # Computer wins:
    if ((computer == plays[0]) and (user == plays[2])) or ((computer == plays[1]) and (user == plays[0])) or ((computer == plays[2]) and (user == plays[1])):
        print('\033[1;31mI win!!')
sleep(1)

print('\n\033[1;35mThank you for playing with me, user ^^. Press the play button to go again!\033[m')
