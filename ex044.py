# Make a program that shows the price to be paid for a product considering the method of payment:
# à vista (money or cash): 10% discount, à vista (card): 5% discount, up to 2x card: normal price, 3x+ card: 20% juros

price = int(input('Product price: R$'))
print("""Choose payment method 
[ 1 ] Cash 
[ 2 ] Card
[ 3 ] 2x card
[ 4 ] 3x+ card):""")

pay_m = str(input('')).strip()

if pay_m == '1':
    price = price - (price * 10 / 100)

elif pay_m == '2':
    price = price - (price * 5 / 100)

elif pay_m == '3':
    price = price / 2

elif pay_m == '4':
    time = int(input('\nMonths: '))
    price = price + (price * (20/100))
    total = price / time


print('\nWith "{}" as a payment method, you will pay R${:.2f} for the product.'.format(pay_m, price))
