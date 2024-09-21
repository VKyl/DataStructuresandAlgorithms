import matplotlib.pyplot as plt
from Pr2.DotsAndLines.Point import Point


class GraphicManager:
    @staticmethod
    def draw(points: list[Point], lines: list[tuple[Point, Point, Point, Point]], label: str = None):
        plt.title(label)
        plt.scatter(list(map(lambda point: point.x, points)), list(map(lambda point: point.y, points)))

        plt.plot(list(map(lambda point: point.x, lines)),
              list(map(lambda point: point.y, lines)))

        plt.show()
