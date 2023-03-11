# Develop a program that asks the distance of a trip (in KM).
# Calculate the price of the trip, charging R$0.50 per KM for trips up to 200km, and R$0.45 for longer trips.

distance = float(input('Type the distance of the trip, in KM: '))

if distance <= 200:
    price = 0.5 * distance
else:
    price = 0.45 * distance

print('The price of the trip is R${:.2f}'.format(price))

# You can also use price = distance * 0.5 if distance <= 200 else distance * 0.45. SIMPLIFIED IF STATEMENT.
