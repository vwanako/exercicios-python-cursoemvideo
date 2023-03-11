# Develop a program that reads 6 whole numbers and shows the sum of the even ones. If the number typed is odd, ignore it

soma = 0

for i in range(1, 7):
    num = int(input('Type number {}: '.format(i)))
    if (num % 2) == 0:
        soma += num
print('The sum between the EVEN numbers you typed was: {}'.format(soma))
