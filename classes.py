# 2. Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс Figure. Создать
# три дочерних класса Circle(атрибуты: координаты центра(тип Point), длина радиуса; методы:
# нахождение периметра и площади окружности),

import math
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure(ABC):

    def calculate_dimension(x, y, x2, y2):
        return math.sqrt(((x2 - x) ** 2) + ((y2 - y) ** 2))

    @abstractmethod
    def perimeter(self, *args):
        pass

    @abstractmethod
    def square(self, *args):
        pass


class Cirlce(Figure):

    def __init__(self, point_x, point_y, radius):
        self.point = Point(point_x, point_y)
        self.radius = radius

    def perimeter(self):
        return 2 * 3.1415 * self.radius

    def square(self):
        return 3.1415 * (self.radius ** 2)


# Triangle(атрибуты: три точки, методы: нахождение площади и периметра),

class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)
        self.point3 = Point(x3, y3)

    def perimeter(self):
        side1 = Triangle.calculate_dimension(self.point1.x, self.point1.y, self.point2.x, self.point2.y)
        side2 = Triangle.calculate_dimension(self.point2.x, self.point2.y, self.point3.x, self.point3.y)
        side3 = Triangle.calculate_dimension(self.point1.x, self.point1.y, self.point3.x, self.point3.y)
        return side1 + side2 + side3

    def square(self):
        side1 = Triangle.calculate_dimension(self.point1.x, self.point1.y, self.point2.x, self.point2.y)
        side2 = Triangle.calculate_dimension(self.point2.x, self.point2.y, self.point3.x, self.point3.y)
        side3 = Triangle.calculate_dimension(self.point1.x, self.point1.y, self.point3.x, self.point3.y)
        s = (side1 + side2 + side3) / 2.0
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


# Square(атрибуты: две точки, методы: нахождение площади и периметра).

class Square(Figure):
    def __init__(self, x1, y1, x2, y2, ):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)

    def perimeter(self):
        side1 = Square.calculate_dimension(self.point1.x, self.point1.y, self.point2.x, self.point2.y)

        return side1 * 4

    def square(self):
        side1 = Triangle.calculate_dimension(self.point1.x, self.point1.y, self.point2.x, self.point2.y)
        return side1 ** 2