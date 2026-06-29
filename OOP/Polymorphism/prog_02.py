#Shape Area Calculator
class Shape:

    def area(self):
        print("Area not defined")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area:", self.length * self.width)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", 3.14 * self.radius * self.radius)


rectangle = Rectangle(5, 4)
circle = Circle(7)

rectangle.area()
circle.area()