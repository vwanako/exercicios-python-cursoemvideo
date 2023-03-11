# Write a program that reads a car's speed. If it is over 80km/h, show a message saying it was fined.
# The fine will cost R$7,00 for each km over the limit.

speed = float(input("Type the car's speed: "))
print("\nThe car is going at {}km/h".format(speed))

if speed > 80:
    fine = (speed - 80) * 7
    print("\nThe speed is {}km over the limit of 80km/h. You will have to pay a fine of R${}.".format(speed - 80, fine))
else:
    print("\nThe car is within the 80km/h speed limit. No fine will be paid.")
