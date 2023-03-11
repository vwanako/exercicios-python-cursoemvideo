# There is another, shorter way to check palindromes in Python:

phrase = str(input('Type a phrase: ')).strip().lower()
words = phrase.split()
join = ''.join(words)

inverse = join[::-1]

if join == inverse:
    print('\033[1;32m{}\033[m is a palindrome'.format(phrase))
else:
    print('\033[1;31m{}\033[m is not a palindrome'.format(phrase))
