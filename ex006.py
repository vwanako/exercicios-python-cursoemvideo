# Create an algorithm that reads a number and shows its double, triple, and it's square root

number = int(input("Hello user, pick a number and I will show its double, triple and it's square root! "))
double = number * 2
triple = number * 3
square_root = number ** (1/2)

print("Your number's:\ndouble is: {}\ntriple is: {}\nsquare root is: {:.2f}".format(double, triple, square_root))
print("Thank you for using my program!")
