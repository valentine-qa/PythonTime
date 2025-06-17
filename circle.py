import math


class Circle:

    version = '0.1'

    def __init__(self, radius):
        self.radius = radius
        self.color = 'color'

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimetr(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0)
        return Circle(radius)

a = Circle(10)
print(a.color)
print(a.area())


class Tire(Circle):

    def perimetr(self):
        return Circle.perimetr(self) * 1.25

# t = Tire(10)
# print(t.radius)
# print(t.area())
# print(t.perimetr())

t = Tire.from_bbd(45)
print(t.radius)
print(t.area())
print(t.perimetr())
