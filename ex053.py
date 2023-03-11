# Make a program that reads a random phrase and says if it is a palindrome, ignoring spaces

phrase = str(input('Type a phrase: ')).strip().lower()
words = phrase.split()
join = ''.join(words)
inverse = ''

for letter in range(len(join) - 1, -1, -1):
    inverse += join[letter]

if join == inverse:
    print('\033[1;32m"{}"\033[m is a palindrome'.format(phrase))

else:
    print('\033[1;31m"{}"\033[m is not a palindrome'.format(phrase))
