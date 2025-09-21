import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the circumference of a circle
def circle_circumference(radius):
    return 2 * math.pi * radius

# Function to calculate the area of a triangle given base and height
def triangle_area(base, height):
    return 0.5 * base * height