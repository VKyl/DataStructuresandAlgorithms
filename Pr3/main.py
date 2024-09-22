from GraphicManager import GraphicManager
from FileManager import FileManager
from ConvexHull import ConvexHull, Point


def test(test_case: list[Point], hull: ConvexHull, graphic: GraphicManager):
    hull.clear()
    hull.points = test_case
    hull.find_hull()
    graphic.draw(hull.points, hull.surface_points)


if __name__ == '__main__':
    file_manager = FileManager('./computer_vision_data')
    convex_hull = ConvexHull()
    graphic_manager = GraphicManager()

    input6 = list(file_manager.read("input6.txt"))
    grid = list(file_manager.read("grid6x6.txt"))
    input8 = list(file_manager.read("input8.txt"))
    input40 = list(file_manager.read("input40.txt"))
    input50 = list(file_manager.read("input50.txt"))
    input56 = list(file_manager.read("input56.txt"))
    input100 = list(file_manager.read("input100.txt"))
    input1423 = list(file_manager.read("rs1423.txt"))

    test_cases = [input6, input8, input40, input50, input56, input100, input1423]

    for test_case in test_cases:
        test(test_case, convex_hull, graphic_manager)
