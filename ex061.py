# re-do challenge 51, reading the first term and reason of a p.a, showing the 10 terms, using while

print('=' * 38)
print('10 TERMS OF AN ARITHMETIC PROGRESSION')
print('=' * 38)

first_term = int(input('First term: '))
r = int(input('The reason is: '))
term = first_term
cont = 1

while cont <= 10:
    print('{}'.format(term), end=' ➝ ')
    term += r
    cont += 1

print('Done!')
