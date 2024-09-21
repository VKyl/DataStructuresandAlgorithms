import math

from Point import Point
from Basis import Basis


class ConvexHull:
    def __init__(self, points: list[Point] = None):
        self.__points = points or []
        self.__surface_points = []

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points: list[Point]):
        self.__points = points.copy()

    @property
    def surface_points(self):
        return self.__surface_points

    def push(self, point: Point):
        self.__surface_points.append(point)

    def pop(self, index: int = -1):
        self.__surface_points.pop(index)

    def clear(self):
        self.__surface_points.clear()

    def __lowest_point(self) -> Point:
        return min(self.points, key=lambda point: point.y)

    def __sort_by_angle(self, base_point: Point) -> list[Point]:
        angles = sorted(self.points, key=lambda point: math.atan2(point.y - base_point.y,
                                                                  point.x - base_point.x))

        return angles

    @staticmethod
    def __is_clockwise(vector, y_basis: Point) -> bool:
        x_basis: Point = Point(y_basis.y, -1 * y_basis.x) if not (y_basis.x >= 0) ^ (y_basis.y >= 0) \
            else Point(-1 * y_basis.y, y_basis.x)
        basis = Basis(x_basis.coords, y_basis.coords)
        return basis.to_basis(vector.coords)[0] > 0

    def find_hull(self):
        lowest_point = self.__lowest_point()
        angle_sorted = self.__sort_by_angle(lowest_point)

        self.__surface_points = [lowest_point, angle_sorted[1]]

        for point in angle_sorted[2:]:
            y_basis = self.__surface_points[-1] - self.__surface_points[-2]
            vector = point - self.__surface_points[-1]

            while self.__is_clockwise(vector, y_basis):
                self.__surface_points.pop()
                y_basis = self.__surface_points[-1] - self.__surface_points[-2]
                vector = point - self.__surface_points[-1]
            self.__surface_points.append(point)

    #TODO перевіряти усі найближчі точки
    # поки є проти годинника
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(\npoints={self.__points},\nsurface_points={self.__surface_points})"
