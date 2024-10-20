class Cell:
    def __init__(self, row: int):
        self._sides: list[bool] = [True, True, True, True]
        self._row = row

    @property
    def row(self):
        return self._row

    def side(self, side: int) -> bool:
        """
            \n 0: top
            \n 1: right
            \n 2: bottom
            \n 3: left
        """
        return self._sides[side]

    def open(self, side: int):
        """
            \n 0: top
            \n 1: right
            \n 2: bottom
            \n 3: left
        """
        self._sides[side] = True

    def close(self, side: int):
        """
            \n 0: top
            \n 1: right
            \n 2: bottom
            \n 3: left
        """
        self._sides[side] = False

    def __repr__(self):
        top = '┌' + ('───' if not self.side(0) else '   ') + '┐'
        mid = ('│' if not self.side(-1) else ' ') + '   ' + ('│' if not self.side(1) else ' ')
        bottom = '└' + ('───' if not self.side(2) else '   ') + '┘'

        return f"{top}\n{mid}\n{bottom}"


if __name__ == '__main__':
    cell1 = Cell(1)
    cell2 = Cell(2)
    cell2.close(1)
    cell2.close(2)

