import copy
import random

from Cell import Cell
from OmegaSet import OmegaSet


class Maze:
    def __init__(self, x_size, y_size):
        self.__x_size = x_size
        self.__y_size = y_size
        self.__maze: list[list[Cell]] = []
        self.__set = OmegaSet()
        self.__create_maze()

    @property
    def maze(self) -> list[list[Cell]]:
        return self.__maze

    @property
    def x_size(self):
        return self.__x_size

    @property
    def y_size(self):
        return self.__y_size

    def __create_maze(self):
        self.__generate_first_row()
        self.__generate_rows()
        self.__generate_borders()
        self.__generate_exits()

    def __generate_first_row(self):
        row = []
        for _ in range(self.__x_size):
            cell = Cell(0)
            row.append(cell)
            self.__set.add_cell(cell)
        self.__place_right(row)
        self.__place_bottom(row, 0)
        self.__maze.append(row)

    def __generate_rows(self):
        for row_index in range(1, self.__y_size):
            row = list(self.__copy_row(self.__maze[-1], row_index))
            self.__remove_right(row)
            self.__place_right(row)
            self.__place_bottom(row, row_index)
            self.__maze.append(row)

    def __generate_borders(self):
        for i in range(self.__x_size):
            self.__maze[0][i].close(0)
            self.__maze[-1][i].close(2)

        for i in range(self.__y_size):
            self.__maze[i][0].close(-1)
            self.__maze[i][-1].close(1)

    def __generate_exits(self):
        self.__maze[0][0].open(-1)
        for i in range(self.__x_size - 1):
            cell = self.__maze[-1][i]
            neighbour = self.__maze[-1][i+1]
            if self.__set.find(cell) != self.__set.find(neighbour):
                cell.open(1)
                self.__set.union(cell, neighbour)
        self.__maze[-1][-1].open(1)

    def __place_right(self, row: list[Cell]):
        for i in range(self.x_size-1):
            if self.__set.find(row[i]) == self.__set.find(row[i+1]):
                row[i].close(1)
                continue
            if random.choice([False, False, False, True]):
                row[i].close(1)
            else:
                self.__set.union(row[i], row[i+1])

    def __place_bottom(self, row: list[Cell], row_index: int):
        for i in range(self.x_size):
            cell = row[i]
            if random.choice([False, True, True, True]):
                cell.close(2)
            if not self.__set.has_open_bottom(cell, row_index):
                cell.open(2)

    def __repr__(self):
        return "\n".join(self._stringify_row(row) for row in self.maze)

    def __copy_row(self, row, row_index):
        for cell in row:
            if cell.side(2):
                new_cell = copy.deepcopy(cell)
            else:
                new_cell = Cell(row_index)
            self.__set.add_cell(new_cell)
            if cell.side(2):
                self.__set.union(cell, new_cell)
            yield new_cell

    @staticmethod
    def __remove_right(row):
        for cell in row:
            cell.open(1)

    @staticmethod
    def __remove_bottom(row):
        for cell in row:
            if cell.side(2):
                cell.open(2)


    @staticmethod
    def _stringify_row(cells):
        top = []
        mid = []
        bottom = []
        for cell in cells:
            cell_lines = repr(cell).split('\n')
            top.append(cell_lines[0])
            mid.append(cell_lines[1])
            bottom.append(cell_lines[2])
        return ' '.join(top) + "\n" + ' '.join(mid) + "\n" + ' '.join(bottom)


if __name__ == '__main__':
    maze = Maze(10, 3)
    print(maze)