from Pr3.GraphicManager import GraphicManager
from Pr3.FileManager import FileManager
from ABComparator import ABComparator
from FastComparator import FastComparator
from BruteForceComporator import BruteForceComparator
from Point import Point


def test(comparator: ABComparator, points: list[Point], graphic: GraphicManager):
    comparator.points = points
    graphic.draw(comparator.points, comparator.find_lines(),
                 f'{type(comparator).__name__}')
    comparator.clear()


if __name__ == '__main__':
    file_manager = FileManager('../../Pr3/computer_vision_data')
    graphic_manager = GraphicManager()
    brute_force = BruteForceComparator()
    fast = FastComparator()

    input6 = list(file_manager.read("input6.txt"))
    input8 = list(file_manager.read("input8.txt"))
    input40 = list(file_manager.read("input40.txt"))
    input50 = list(file_manager.read("input50.txt"))
    input56 = list(file_manager.read("input56.txt"))
    input100 = list(file_manager.read("input100.txt"))
    input1423 = list(file_manager.read("rs1423.txt"))

    test_cases = [input6, input8, input40, input50, input56, input100, input1423]

    for test_case in test_cases:
        test(fast, test_case, graphic_manager)
    #
    # for test_case in test_cases:
    #     test(brute_force, test_case, graphic_manager)
