import math


class GeometricForm:
    def __init__(self):
        pass

    def getArea(self):
        pass

    def getPerimeter(self):
        pass


class Circle(GeometricForm):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getPerimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(GeometricForm):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

c = Circle(5)
print(c.getArea())
print(c.getPerimeter())

d = Rectangle(4, 5)
print(d.getArea())
print(d.getPerimeter())
