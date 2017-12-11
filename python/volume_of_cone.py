import math

radius = float(input("Enter radius of cone: "))
height = float(input("Enter height of cone: "))
volume = math.pi * radius**2 * height/3

print("The volume of a cone with radius", radius, "and height", height, "is", round(volume,1))