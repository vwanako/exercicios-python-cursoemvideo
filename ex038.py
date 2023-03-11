# Write a program that reads 2 whole numbers and compares them, displaying on the screen a message:
# The first number is bigger, the second number is bigger or there is no bigger value, they're equal

n1 = int(input('First number: '))
n2 = int(input('Second number: '))

if n1 > n2:
    print('The first number, {}, is bigger'.format(n1))
elif n1 < n2:
    print('The second number, {}, is bigger'.format(n2))
else:
    print('The numbers are equal, there is no bigger number')
