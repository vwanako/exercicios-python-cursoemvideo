# M.a.p that reads a phrase and says: how many times the "A" appears, the first position it appears, and last position

phrase = input("Type a phrase: ").strip().lower()

print("The letter A shows up {} times in the phrase.".format(phrase.count('a')))
print("The letter A shows up first in the index {} and last in the index {}".format(phrase.find('a'), phrase.rfind('a')))
