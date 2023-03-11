# Create a program that reads the name and price of multiple products. Ask the user if they would like to continue or
# not. Show: a) the total price of the purchase b) how many products are over R$1000 c) the cheapest product's name

products = total = po1k = smallest_price = smallest_name = 0

while True:
    name = str(input('\nProduct name: '))
    price = float(input('Price: R$'))
    total += price
    products += 1

    if price >= 1000:
        po1k += 1

    if products == 1:
        smallest_price = price
        smallest_name = name
    else:
        if price < smallest_price:
            smallest_price = price
            smallest_name = name

    user = str(input('Continue [Y/N]? '))
    while user not in 'YyNn':
        user = str(input('Invalid option. Continue [Y/N]? '))

    if user in 'Nn':
        break

print(f'The total was {total:.2f}. There are {po1k} products over R$1000. The cheapest product was {smallest_name}')
