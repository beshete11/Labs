import math

radius = float(input("Enter radius: "))
area = float("{:.2f}".format(radius * radius * math.pi))
circumference = float("{:.2f}".format(2 * math.pi * radius))

print("The circle with radius", radius, "has an area of", area, "and a perimeter of", circumference)