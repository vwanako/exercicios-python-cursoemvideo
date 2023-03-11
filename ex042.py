# Re-do challenge 035 and add a resource that shows what type of triangle is formed.
# Equilateral: all equal sides, Isosceles: two equal sides, Scalene: all different sides

print('\033[1;34m-+-' * 8)
print('Triangle analyser 2.0')
print('-+-' * 8)

r1 = float(input('\033[mFirst side: '))
r2 = float(input('Second side: '))
r3 = float(input('Third side: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('\n\033[1;32mYou CAN make a triangle\033[m with sides {}, {} and {}.'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('The triangle formed is \033[1;34mequilateral\033[m.')
    elif (r1 == r2 != r3) or (r1 != r2 == r3) or (r1 == r3 != r2):
        print('The triangle formed is \033[1;34misosceles\033[m.')
    elif r1 != r2 != r3:
        print('The triangle formed is \033[1;34mscalene\033[m.')
else:
    print('\033[1;31mYou can NOT make a triangle with sides {}, {} and {}'.format(r1, r2, r3))
