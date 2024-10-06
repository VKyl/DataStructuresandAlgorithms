class Board:
    def __init__(self, dimension, blocks) -> None:
        self._dimension = dimension
        self._blocks = blocks

    def dimension(self) -> int:
        return self._dimension

    def hamming(self) -> int:
        # hamming distance
        pass

    def manhattan(self) -> int:
        # manhattan distance
        pass

    def is_goal(self) -> bool:
        # check if this board is solution
        pass

    def __eq__(self, other) -> bool:
        # check that this board is equal to other
        pass

    def neighbors(self) -> list:
        # should return list of neighbor boards
        pass

    def __str__(self) -> str:
        # string representation
        pass
