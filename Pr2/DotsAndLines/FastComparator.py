from ABComparator import ABComparator
from Point import Point


class FastComparator(ABComparator):
    def __init__(self, points: list[Point] = None):
        super().__init__(points)

    def find_lines(self):
        for point in self.points:
            slope_sort = sorted(self.points, key=lambda p: point.slope_to(p))
            self.__search_collinear(point, slope_sort)
        return self._lines

    def __search_collinear(self, point: Point,  slope_sort: list[Point]):
        for window_end in range(3, len(slope_sort)):
            point1, point2, point3 = (slope_sort[window_end - 2],
                                      slope_sort[window_end - 1],
                                      slope_sort[window_end])

            if self._in_line(point, point1, point2, point3):
                #print(f'{point} -> {point1} -> {point2} ->{point3}')
                self._lines.append((point, point1, point2, point3))

    def __str__(self):
        return f"FastComparator(points={', '.join(self.parsed_points)})"
