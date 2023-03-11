# Make a program that reads a number between 0 and 9999 and shows its digit separated (unidade, dezena, centena, milhar)

number = int(input('Please type a number between 0 and 9999'))

thousand = number // 1000 % 10
hundred = number // 100 % 10
ten = number // 10 % 10
units = number // 1 % 10

print("Your number is {}. It has {} milhares, {} centenas, {} dezenas and {} unidades".format(number, thousand, hundred, ten, units))

