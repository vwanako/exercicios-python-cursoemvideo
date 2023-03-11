# program that reads multiple whole numbers the program stops if the number typed is 999.
# in the end, show how many numbers were typed and what their sum was (except for 999)
cont = soma = 0

num = int(input('Type a number [999 to stop]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Type a number [999 to stop]: '))

print('Sum = {}'.format(soma))
