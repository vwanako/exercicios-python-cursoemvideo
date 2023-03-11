# Make a program that reads height and width of a wall in meters
# Calculate the area and amount of paint needed to paint the wall, knowing that 1l = 2m²

print("Welcome, user, I will calculate the amount of paint you will need to paint the a wall.")
wall_height = float(input("What is the height of the wall? "))
wall_width = float(input("What is the width of the wall? "))

wall_area = wall_width * wall_height
paint_needed = wall_area / 2

print("The area of the wall is {:.2f}m², you will use {:.2f} liters of paint to paint it.".format(wall_area, paint_needed))
