# Make a program that makes the computer "think" in a whole number (0-5) and make the user try to guess the number
# The program should tell the user whether they won or not

from random import randint

print("-=-" * 20)
print("Hey user, let's play a game! I will think of a whole number from 0 to 5, and you have to guess it")
print("\nIf you guess right, you win, if you don't, I win. Let me think... Ok, got it!")
print("-=-" * 20)

computer_number = randint(0, 5)

user_guess = int(input('\nYour turn now, guess the number I thought of! '))

if user_guess == computer_number:
    print("Yes, it was number {}. You did it! Congrats, user, you won!!.".format(computer_number))
else:
    print("Oh, I'm sorry user, it was {}, not {}. I win!".format(computer_number, user_guess))

print("\nThank you for playing with me, user ٩(｡•́‿•̀｡)۶! Press the play button to go again!")
