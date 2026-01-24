class Rectangle:

    def __int__(self):
        self.length = 0
        self.width = 0

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def area(self):
     return self.length * self.width


# Example usage
r = Rectangle()
r.set_width(10)
r.set_length(20)

print("Length:", r.get_length())
print("Width:", r.get_width())
print("area:", r.area())
