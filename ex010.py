# Create a program that reads how much money the user has in their wallet, and how many dollars they can buy (R$3.27)

real = float(input("Welcome to the DollarStore. How much money do you currently have? R$"))
dollar = real / 3.27

print("You can buy ${:.2f} with R${:.2f}!".format(dollar, real))
