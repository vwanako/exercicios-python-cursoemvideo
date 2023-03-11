# Create a program that shows the multiplication table of multiple numbers that the user types and stops when the number
# typed is negative.

num = 0
mult = 1

while num >= 0:
    num = int(input('Type a number: '))
    if num < 0:
        break
    print('=' * 20)
    while mult <= 10:
        print(f'{num} x {mult} = {num * mult}')
        mult += 1
    mult = 1
    print('=' * 20)

print('DONE!')
