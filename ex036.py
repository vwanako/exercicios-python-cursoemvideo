# Write a program that allows a loan for the purchase of a house.
# The program will ask the house's price, the buyer's income and in how many years they will pay.
# Calculate the value of the monthly price, knowing it can not exceed 30% of the buyer's income, or it will be denied.

house_price = float(input('House price: R$'))
income = float(input("Buyer's income: R$"))
years = int(input("Years the house will be paid in: "))
monthly_price = house_price / (years * 12)

print("The monthly payment will be \033[1;34mR${:.2f}\033[m.".format(monthly_price))

if monthly_price > (income * 30 / 100):
    print("\033[1;31mLoan denied.\033[m Buyer can not afford the house.")
else:
    print("\033[1;32mLoan approved.\033[m Buyer can afford the house.")
