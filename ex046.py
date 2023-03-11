# Make a program that counts from 10 to 0 for a firework display, with a pause of 1 second between them

from time import sleep

print('Firework countdown!!!')
sleep(1)

time = 10

for i in range(10, -1, -1):
    print(time,)
    time -= 1
    sleep(1)

print('KABOOM!!')

