# make a program that reads a random number and shows its factorial.

n = int(input('Type a number: '))
fact = n - 1

while fact != 1:
    n *= fact
    fact -= 1

print('The factorial is: {}'.format(n))
