# make a program that reads a random angle and displays its sine, cosine and tangent.

from math import sin, cos, radians, tan

angle = float(input("Type an angle: "))
radian = radians(angle)
sine = sin(radian)
cosine = cos(radian)
tangent = tan(radian)

print("The sine is {:.4f}, the cosine is {:.4f} and the tangent is {:.4f}".format(sine, cosine, tangent))
