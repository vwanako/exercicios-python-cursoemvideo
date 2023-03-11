# Create a program that has a tuple with the written count of zero to twenty. Read the user's inputed number and write
# it with your tuple.

ext = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
       'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

uinput = int(input('Type a number: '))

print(f'You number is {ext[uinput]}')
