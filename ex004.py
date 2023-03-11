# 4th challenge: make a program that reads something the user types, and show its type and all the information you can

print('Welcome to the amazing TEXT INFORMATION FUNCTION!! Type anything and I will tell you about what you wrote.')

user_text = input(" ")

print("Is your text:")
print("A string, boolean, integer or float?", type(user_text))
print("Numeric?", user_text.isnumeric())
print("Alphabetical?", user_text.isalpha())
print("Alphanumerical?", user_text.isalnum())
print("All upper case?", user_text.isupper())
print("All lower case?", user_text.islower())
print("Printable?", user_text.isprintable())
print("Ascii?", user_text.isascii())
print("Capitalized?", user_text.istitle())
