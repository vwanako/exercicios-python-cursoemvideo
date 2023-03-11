# Make a program that reads a random whole number and shows its multiplication table

number = int(input("Hello user, please type a number and I will show you it's multiplication table! "))
multiplier = 1

print("-" * 12)

while multiplier <= 10:
    print("{} x {} =".format(number, multiplier), number * multiplier)
    multiplier += 1

print("-" * 12)
