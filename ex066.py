# Create a program that reads multiple whole numbers. The program stops when the user types 999. Sum the numbers without
# the flag

user = soma = 0

while True:
    user = int(input('Type a number [999 to stop]: '))
    if user == 999:
        break
    soma += user

print(soma)
