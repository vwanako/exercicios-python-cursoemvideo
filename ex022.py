# Create a program that reads a person's name and shows it: in all caps, in all lowercase, how many letters there
# are, how many letters in the first name.

name = str(input('What is your name? '))
name = name.strip()

print("Here's your name in upper case {}".format(name.upper()))
print("Here's your name in lower case {}".format(name.lower()))

name_list = name.split()
first_name = name_list[0]
spaces = name.count(' ')

print("Your first name is {} and has {} letters".format(first_name, len(first_name)))
print("Your whole name has {} letters".format(len(name) - spaces))
