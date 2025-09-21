import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    try:
        length, width = float(length), float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return length * width
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    try:
        length, width = float(length), float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Function to calculate the area of a circle
def circle_area(radius):
    try:
        radius = float(radius)
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return math.pi * radius ** 2
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Function to calculate the circumference of a circle
def circle_circumference(radius):
    try:
        radius = float(radius)
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return 2 * math.pi * radius
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Function to calculate the area of a triangle
def triangle_area(base, height):
    try:
        base, height = float(base), float(height)
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height
    except (ValueError, TypeError) as e:
        return f"Error: {e}"

# Main function to test the module
if __name__ == "__main__":
    test_cases = [
        ("Rectangle Area", rectangle_area, (5, 3)),
        ("Rectangle Perimeter", rectangle_perimeter, (5, 3)),
        ("Circle Area", circle_area, (4,)),
        ("Circle Circumference", circle_circumference, (4,)),
        ("Triangle Area", triangle_area, (6, 8)),
        ("Invalid Rectangle", rectangle_area, (-5, 3)),
        ("Invalid Circle", circle_area, ("abc",)),
        ("Invalid Triangle", triangle_area, (6, -8)),
    ]

    for name, func, args in test_cases:
        print(f"{name}: {func(*args)}")