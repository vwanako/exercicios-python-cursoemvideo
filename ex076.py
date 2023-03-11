# create a program that has a tuple with products' names and prices in sequence, in the end show a list of prices.

products = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90, 'Estojo', 25.00,'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('='*40)
print('Listagem de preços:')
print('='*40)

for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}R$', end=' ')
    else:
        print(f'{products[pos]:>7.2f}')

print('='*40)
