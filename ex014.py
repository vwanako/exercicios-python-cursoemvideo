# Write a program that converts a temperature in ºC to ºF

celsius = float(input("The temperature in celsius is:"))
fahrenheit = (celsius * 1.8) + 32

print("{}ºC is {:.2f}ºF.".format(celsius, fahrenheit))
