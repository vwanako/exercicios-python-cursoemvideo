# Make a program that reads a city's name and says if it begins or not with "Santo"

city = input("Type the name of a city: ")
city = city.strip()
city = city.split(' ')

if city[0] == "Santo":
    print("The city's name begins with 'Santo'")
elif city[0] != "Santo":
    print("The city's name doesn't begin with 'Santo'")


# Another way:

city = input("Type the name of a city: ")
city = city.lower()
city = city.strip()

print(city[:5] == 'santo')
