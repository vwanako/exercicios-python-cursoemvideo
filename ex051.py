# Develop a program that reads the first term and the reason of a P.A, show the first 10 terms

print('=' * 38)
print('10 TERMS OF AN ARITHMETIC PROGRESSION')
print('=' * 38)

first_term = int(input('First term: '))
r = int(input('R: '))
tenth = first_term + (10 - 1) * r

for i in range(first_term, tenth + r, r):
    print('{}'.format(i), end=' ➝ ')

print('Done!')
