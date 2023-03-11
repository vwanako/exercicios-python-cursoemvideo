# create a program that has a tuple with multiple words and shows the vowels of each word.
# my idea: i could use string slicing where i count each letter and if it's in 'aeiou' i print it?

words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')

for word in words:
    print(f'\n The word {word} has the vowels', end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'\033[32m{letter}\033[0m', end=' ')