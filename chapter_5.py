# A base class to define a Shape
class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Square(Shape):
    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Triangle(Shape):
    def calculate_area(self):
        return 0.5 * self.height * self.width

    def calculate_perimeter(self):
        return 3 * self.height


class Circle(Shape):
    def __init__(self, height):
        super().__init__(height, height)
        self.radius = height / 2

    def calculate_area(self):
        return 3.14 * (self.radius * self.radius)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


def main():
    square = Square(5, 5)
    print(square.calculate_area())
    print(square.calculate_perimeter())

    triangle = Triangle(5, 5)
    print(triangle.calculate_area())
    print(triangle.calculate_perimeter())

    circle = Circle(5)
    print(circle.calculate_area())
    print(circle.calculate_perimeter())


main()
