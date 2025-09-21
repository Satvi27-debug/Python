import math

# Function to calculate distance
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Taking user input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculating distance
distance = distance_between_points(x1, y1, x2, y2)

# Displaying result
print(f"Distance between points: {distance:.2f}")