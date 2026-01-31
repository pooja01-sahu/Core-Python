from typing import List


class Shape:

    def area(self):
        print("Shape area method")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print("Rectangle area", rectangle_area)
        return rectangle_area


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.radius * self.radius
        print("Circle area", circle_area)
        return circle_area

    # Define a list of shape object


shapes: List[Shape] = [Rectangle(10, 20), Circle(20)]

# Loop over the list and call area
for shape in shapes:
    shape.area()
