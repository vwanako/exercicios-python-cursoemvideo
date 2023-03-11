# Develop a program that reads the size of three lines and tells the user if they can or not form a triangle.
# (Look for triangle formation rules)

print("-+-" * 6)
print("Triangle analyser: ")
print("-+-" * 6)

r1 = float(input('First side: '))
r2 = float(input('Second side: '))
r3 = float(input('Third side: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("You CAN form a triangle with sides: {}, {} and {}.".format(r1, r2, r3))
else:
    print("You can NOT form a triangle with sides: {}, {} and {}.".format(r1, r2, r3))
