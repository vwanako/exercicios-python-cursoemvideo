# Make an algorithm that reads the price of a product, and its new price with 5% discount

original_price = float(input("How much is the product before the discount? R$"))
new_price = original_price - (original_price * 5 / 100)

print("The new price is R${:.2f}".format(new_price))
