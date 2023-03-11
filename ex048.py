# Make a program that sums all the odd numbers that are multiples of 3 between 1 and 500

soma = 0
cont = 0

for i in range(1, 501, 2):
    if (i % 3) == 0:
        cont += 1
        soma += i

print('The sum of the {} values is {}'.format(cont, soma))
