import random
from wqu.weighted_quick_union import WeightedQuickUnion


class Percolation:
    def __init__(self, number: int):
        """
        create NxN matrix with all closed cells
        :param number: <int> number of rows and columns
        """
        self._number = number
        self._opened = 0

        self._matrix = [[False for _ in range(number)] for _ in range(number)]
        self._WQU = WeightedQuickUnion(number ** 2 + 2)
        self._top_bottom_union()

    @property
    def opened_count(self) -> int:
        """
        opened cells count
        :return: <int> opened cells count
        """
        return self._opened

    def start(self):
        while not self._percolates():
            i = random.randint(0, self._number - 1)
            j = random.randint(0, self._number - 1)
            self._open(i, j)

    def _top_bottom_union(self):
        for i in range(self._number):
            self._WQU.union(i, self._number**2)
            self._WQU.union(self._number * (self._number - 1) + i, self._number**2 + 1)

    def _open(self, i: int, j: int):
        """
        open cell that is not opened yet
        :param i: <int> row index
        :param j: <int> column index
        """
        if self._is_opened(i, j):
            return

        self._matrix[i][j] = True

        self._union((i, j), (i-1, j))
        self._union((i, j), (i+1, j))
        self._union((i, j), (i, j-1))
        self._union((i, j), (i, j+1))

        self._opened += 1

    def _union(self, main_cell: tuple[int, int], other_cell: tuple[int, int]):
        if self._in_matrix(*other_cell) and self._is_opened(*other_cell):
            self._WQU.union(main_cell[0] * self._number + main_cell[1],
                            other_cell[0] * self._number + other_cell[1])

    def _in_matrix(self, row, column) -> bool:
        return 0 <= row < self._number and 0 <= column < self._number

    def _is_opened(self, i: int, j: int) -> bool:
        """
        check if cell is opened yet
        :param i: <int> row index
        :param j: <int> column index
        :return: <bool> is cell opened
        """
        return self._matrix[i][j]

    def _percolates(self) -> bool:
        """
        check if system percolates
        :return: <bool> percolates
        """
        return self._WQU.connected(self._number**2, self._number**2+1)

    def __str__(self):
        string = ""
        for row in self._matrix:
            for cell in row:
                string += f'{cell} '
            string += '\n'
        return string
