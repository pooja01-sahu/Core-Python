class Shape:
    def __init__(self, color, borderwidth):
        self.color = color
        self.borderwidth = borderwidth

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setBorderwidth(self, borderwidth):
        self.borderwidth = borderwidth

    def getBorderwidth(self):
        return self.borderwidth


class Rectangular(Shape):

    def __init__(self, length=0, width=0, color="", borderwidth=0):
        self.length = length
        self.width = width
        super().__init__(color, borderwidth)

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width


r = Rectangular(10, 20, "Yellow", 100)
print("Rectangle")
print("Length", r.getLength())
print("width", r.getWidth())
print("color", r.getColor())
print("BorderWidth", r.getBorderwidth())
