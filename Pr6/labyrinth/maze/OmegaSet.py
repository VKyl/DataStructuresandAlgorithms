from Cell import Cell


class OmegaSet:
    def __init__(self):
        self._parent = {}
        self._rank = {}

    def find(self, cell):
        if self._parent[cell] != cell:
            self._parent[cell] = self.find(self._parent[cell])
        return self._parent[cell]

    def union(self, cell1, cell2):
        root1 = self.find(cell1)
        root2 = self.find(cell2)

        if root1 == root2:
            return

        if self._rank[root1] > self._rank[root2]:
            self._parent[root2] = root1
        elif self._rank[root1] < self._rank[root2]:
            self._parent[root1] = root2
        else:
            self._parent[root2] = root1
            self._rank[root1] += 1

    def add_cell(self, cell):
        if cell not in self._parent:
            self._parent[cell] = cell
            self._rank[cell] = 0

    def has_open_bottom(self, cell, row):
        root = self.find(cell)
        for cell in self._parent:
            if self.find(cell) == root and cell.side(2) and cell.row == row:
                return True
        return False


if __name__ == '__main__':
    ds = OmegaSet()
    cellA = Cell(0)
    cellA.close(2)
    ds.add_cell(cellA)
    print(ds.has_open_bottom(cellA, 0))
