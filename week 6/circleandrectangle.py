import tkinter as tk

class Rectangle:
    def __init__(self, x1, y1, x2, y2, color="black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

def draw_rectangle(canvas, rectangle):
    canvas.create_rectangle(rectangle.x1, rectangle.y1, rectangle.x2, rectangle.y2, fill=rectangle.color)

class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

def draw_point(canvas, point):
    radius = 3  # Small circle to represent a point
    canvas.create_oval(point.x - radius, point.y - radius, point.x + radius, point.y + radius, fill=point.color)

class Circle:
    def __init__(self, x, y, radius, color="black"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

def draw_circle(canvas, circle):
    canvas.create_oval(circle.x - circle.radius, circle.y - circle.radius, circle.x + circle.radius, circle.y + circle.radius, fill=circle.color)

# Example usage
def main():
    root = tk.Tk()
    root.title("Canvas Drawing")
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    rect = Rectangle(50, 50, 150, 100, "red")
    draw_rectangle(canvas, rect)

    point = Point(200, 200, "blue")
    draw_point(canvas, point)

    circle = Circle(300, 300, 50, "green")
    draw_circle(canvas, circle)

    root.mainloop()

if __name__ == "__main__":
    main()
