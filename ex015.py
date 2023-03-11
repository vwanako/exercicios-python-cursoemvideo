# Write a program that asks the km that a car ran, and the amount of days it was rented for.
# Then, calculate the price to be paid, knowing the car costs R$60 per day, and R$0,15 per km ran.

days_rented = int(input("For how many days was the car rented? "))
km_ran = float(input("How many kilometers did the car run? "))

to_be_paid = (days_rented * 60) + (km_ran * 0.15)

print("The amount to be paid is of R${:.2f}".format(to_be_paid))
