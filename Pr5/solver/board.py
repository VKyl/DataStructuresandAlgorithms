class Board:
    def __init__(self, dimension, blocks) -> None:
        self._dimension = dimension
        self._blocks = blocks
    # blocks = [0,1,2,
    #           3,4,5,
    #           6,7,8]

    @property
    def blocks(self):
        return self._blocks

    def dimension(self) -> int:
        return self._dimension

    def hamming(self) -> int:
        counter = 0
        for index, block in enumerate(self._blocks):
            if block and (index + 1) != block:
                counter += 1
        return counter

    def manhattan(self) -> int:
        distance = 0
        for index, block in enumerate(self._blocks):
            if block:
                row = index // self._dimension
                col = index % self._dimension
                desired_row = (block - 1) // self._dimension
                desired_col = (block - 1) % self._dimension
                distance += abs(desired_row - row) + abs(desired_col - col)
        return distance

    def is_goal(self) -> bool:
        return not self.hamming()

    def neighbors(self) -> list['Board']:
        neighbors_list = []
        zero_index = self._blocks.index(0)
        row = zero_index // self._dimension
        col = zero_index % self._dimension
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            new_row = dxrow if 0 <= (dxrow := row + dx) < self._dimension else row
            new_col = dyrow if 0 <= (dyrow := col + dy) < self._dimension else col
            if new_row != row or new_col != col:
                new_blocks = self._blocks.copy()
                new_index = new_row * self._dimension + new_col
                new_blocks[new_index], new_blocks[zero_index] = (new_blocks[zero_index], new_blocks[new_index])
                neighbor = Board(self._dimension, new_blocks)
                neighbors_list.append(neighbor)

        return neighbors_list

    def __eq__(self, other: 'Board') -> bool:
        if other is None:
            return False
        return self._blocks == other.blocks

    def __lt__(self, other):
        if self == other and self.hamming() != other.hamming():
            return self.hamming() < other.hamming()
        return self.manhattan() + self.hamming() < other.manhattan() + other.hamming()

    def __str__(self) -> str:
        res = ""
        for index, block in enumerate(self._blocks):
            res += f'{block} ' if index % self._dimension != 2 else f'{block}\n'
        return res

    def __hash__(self) -> int:
        return hash(tuple(self._blocks))


if __name__ == '__main__':
    board = Board(3, [1, 2, 3,
                                       4, 5, 6,
                                       7, 8, 0])
    print(board.hamming())
    print(board.manhattan())
    print(board.is_goal())
    neighbors = board.neighbors()
    print(board)
    for neighbor in neighbors:
        print(neighbor)
