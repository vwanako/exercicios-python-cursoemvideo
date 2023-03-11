# Make a program that reads someone's name and says if it has "Silva" or not

name = input("Type your name: ")
name = name.strip()
name = name.lower()

print('Seu nome tem Silva? {}'.format('silva' in name))

# Way #2
name = input("Type your name: ")
name = name.strip()
name = name.lower()

if name.find('silva'):
    print("The name has 'Silva'")
