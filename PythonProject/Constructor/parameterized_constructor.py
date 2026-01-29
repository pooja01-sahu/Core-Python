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

# with parameterized constructor
s = Shape("red", 2)
print(s.color)
print(s.borderwidth)

# without parameterrized constructor
s.setColor("Pink")
s.setBorderwidth(6)
print("color",s.getColor())
print("borderwidth",s.getBorderwidth())


