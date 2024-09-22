import math
from Point import Point
from Basis import Basis
import matplotlib as mt


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

    def __sort_by_angle(self, base_point: Point):
        def sorting_key(point: Point):
            angle = math.atan2(point.y - base_point.y, point.x - base_point.x)
            return angle, point.distance(base_point)
        self.__points.sort(key=sorting_key)

    def __find_points(self):
        for point in self.__points[2:]:
            while len(self.__surface_points) > 1 and self.__is_clockwise(self.__surface_points[-2],
                                                                         self.__surface_points[-1], point):
                self.__surface_points.pop()
            self.__surface_points.append(point)

    def find_hull(self):
        if len(self.__points) < 3:
            return

        lowest_point = self.__lowest_point()
        self.__sort_by_angle(lowest_point)

        self.__surface_points = [self.__points[0], self.__points[1]]
        self.__find_points()
        self.__surface_points.append(lowest_point)

    @staticmethod
    def __is_clockwise(vector_start: Point, vector_end: Point, point: Point) -> bool:
        y_basis = vector_end - vector_start
        x_basis = Point(-y_basis.y, y_basis.x)
        basis = Basis(x_basis.coords, y_basis.coords)

        vector = point - vector_end
        new_vector = basis.to_basis(vector.coords)
        return new_vector[0] <= 0

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(\npoints={self.__points},\nsurface_points={self.__surface_points})"
