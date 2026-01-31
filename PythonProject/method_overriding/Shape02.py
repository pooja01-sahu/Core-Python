class Shape:

    def execute(self):
        if self.validate():
            self.area()
        else:
            print("Validation Failed")

    def validate(self):
        return False

    def area(self):
        print("Shape area method")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate(self):
        if self.length > 0 and self.width > 0:
            return True
        else:
            return False

    def area(self):
        rectangle_area = self.length * self.width
        print("Rectangle area", rectangle_area)
        return rectangle_area

class Circle(Shape):

    PI = 3.14

    def __init__(self, radius):
       self.radius = radius

    def validate(self):
        if self.radius > 0:
            return True
        else:
            return False

    def area(self):
        circle_area = self.radius * self.radius * self.PI
        print("Circle area", circle_area)
        return circle_area

class Test(Shape):
    pass


r = Rectangle(100, 200)
r.execute()

cr = Circle(10)
cr.execute()

ts = Test()
ts.execute()
