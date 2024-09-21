import math


class Point:
    def __init__(self, x: float or int, y: float or int):
        self.__x: float = float(x)
        self.__y: float = float(y)

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def coords(self):
        return self.__x, self.__y

    def slope_to(self, other: 'Point') -> float:
        self.__validate_type(other)
        if self == other:
            return -math.inf
        if self.x == other.x:
            return math.inf
        return (self.y - other.y) / (self.x - other.x)

    @staticmethod
    def __validate_type(other):
        if type(other) is not Point:
            raise TypeError(f"Object {other} is not of {Point}")

    def __sub__(self, other: 'Point'):
        self.__validate_type(other)
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other: 'Point'):
        self.__validate_type(other)
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __eq__(self, other: 'Point'):
        self.__validate_type(other)
        return self.y == other.y and self.x == other.x

    def __str__(self):
        return f"({self.x}, {self.y})"
