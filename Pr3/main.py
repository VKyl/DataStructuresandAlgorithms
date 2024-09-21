from GraphicManager import GraphicManager
from FileManager import FileManager
from ConvexHull import ConvexHull


if __name__ == '__main__':
    file_manager = FileManager('./computer_vision_data')
    convex_hull = ConvexHull()
    graphic_manager = GraphicManager()

    input6 = list(file_manager.read("input6.txt"))
    input8 = list(file_manager.read("input8.txt"))
    input40 = list(file_manager.read("input40.txt"))
    input50 = list(file_manager.read("input50.txt"))
    input56 = list(file_manager.read("input56.txt"))
    input100 = list(file_manager.read("input100.txt"))
    input1423 = list(file_manager.read("rs1423.txt"))

    convex_hull.points = input8
    convex_hull.find_hull()
    graphic_manager.draw(convex_hull.points, convex_hull.surface_points)
    #
    # test_cases = [input6, input8, input40, input50, input56, input100, input1423]
