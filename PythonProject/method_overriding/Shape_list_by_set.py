from typing import List

class Shape:

    def area(self):
        print("Shape area method")

class Rectangle(Shape):

    def __init__(self):
        self.length = 0
        self.width = 0

    def setLength(self, l):
            self.length = l

    def getLength(self):
            return self.length

    def setWidth(self, w):
            self.width = w

    def getWidth(self):
            return self.width

    def area(self):
      rectangle_area = self.length * self.width
      print("rectangle area", rectangle_area)
      return rectangle_area

class Circle(Shape):

    def __init__(self):
        self.radius = 0

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def area(self):
        circle_area = self.radius * self.radius
        print("circle area", circle_area)
        return circle_area

shapes: List[Shape] = [Rectangle(),Circle()]

rect: Rectangle = shapes[0]
rect.setLength(20)
rect.setWidth(10)


cir: Circle = shapes[1]
cir.setRadius(10)

for shape in shapes:
        shape.area()
