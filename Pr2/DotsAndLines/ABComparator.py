from abc import ABC, abstractmethod
import Point


class ABComparator(ABC):
    def __init__(self, points: list[Point.Point] = None):
        self._points: list[Point.Point] = points if points else []
        self._lines: list[tuple[Point.Point, Point.Point, Point.Point, Point.Point]] = []

    @property
    def points(self) -> list[Point.Point]:
        return self._points.copy() if self._points is not None else []

    @points.setter
    def points(self, points: list[Point.Point]):
        if type(points) is not list[Point.Point]:
            self._points = points

    @property
    def parsed_points(self):
        return list(map(lambda point: point.coords, self._points))

    @property
    def lines(self) -> list[tuple[Point.Point, Point.Point, Point.Point, Point.Point]]:
        return self._lines.copy() if self._lines is not None else []

    def append(self, point: Point.Point):
        if type(point) is not Point.Point:
            raise TypeError(f"Point.Point must be of type {type(Point.Point)}.")
        self._points.append(point)

    def pop(self, index: int = None):
        return self._points.pop(index) if index else self._points.pop()

    def clear(self):
        self._points.clear()
        self._lines.clear()

    @staticmethod
    def _in_line(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
        return ((p1.slope_to(p2) == p2.slope_to(p3) == p3.slope_to(p4) or
                p1.x == p2.x == p3.x == p4.x))

    @abstractmethod
    def find_lines(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
