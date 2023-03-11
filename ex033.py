# Make a program that reads 3 numbers and shows which is bigger and which is smaller

a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))

# Checking the smallest value
smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

# Checking the biggest value
biggest = a
if b > a and b > c:
    biggest = b
if c > a and c > b:
    biggest = c

print("The smallest value typed was: {}".format(smallest))
print("The biggest value types was: {}".format(biggest))
