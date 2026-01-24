from Inheritence.Shape import Shape


class Rectangle(Shape):

    def __init__(self):
        self.width = 0
        self.lenght = 0

    def setwidth(self, width):
        self.width = width

    def getwidth(self):
        return self.width

    def setLength(self, length):
        self.lenght = length

    def getlength(self):
        return self.lenght


r = Rectangle()
r.setwidth(10)
r.setLength(5)
r.setBorderWidth(5)
r.setColor("Pink")

print("width", r.getwidth())
print("length", r.getlength())
print("BorderWidth", r.getBorderwidth())
print("Color", r.getColor())
