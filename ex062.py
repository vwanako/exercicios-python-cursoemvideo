# better challenge 62, asking if the user wants to display more terms. The program ends when they say '0'

print('=' * 38)
print('10 TERMS OF AN ARITHMETIC PROGRESSION')
print('=' * 38)

first_term = int(input('First term: '))
r = int(input('The reason is: '))
term = first_term
cont = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while cont <= 10:
        print('{}'.format(term), end=' ➝ ')
        term += r
        cont += 1
    more = int(input('How many more terms would you like to see? '))

print('Done!')
