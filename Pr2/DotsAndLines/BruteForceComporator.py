from itertools import combinations
from ABComparator import ABComparator
from Point import Point


class BruteForceComparator(ABComparator):
    def __init__(self, points: list[Point] = None):
        super().__init__(points)

    def find_lines(self):
        for point1, point2, point3, point4 in combinations(self._points, 4):
            if self._in_line(point1, point2, point3, point4):
                self._lines.append((point1, point2, point3, point4))
                print(f'{point1} -> {point2} -> {point3} ->{point4}')

        return self._lines

    def __str__(self):
        return f"BrutForceComparator(points={', '.join(self.parsed_points)})"
