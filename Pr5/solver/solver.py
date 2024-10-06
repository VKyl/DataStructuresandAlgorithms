from board import Board


class Solver:
    def __init__(self, board):
        self._initial_board = board

    def is_solvable(self) -> bool:
        # check if board is solvable
        pass

    def moves(self) -> int:
        # return minimal count of steps to solution or -1 if it does not have it
        pass

    def solution(self) -> list:
        # list of sequence of boards in the shortest path or null if we do not have solution
        pass


def read_board_data() -> tuple[int, list[list[int]]]:
    # read dimension and initial list[][] from file
    pass


def main():
    board = Board(*read_board_data())
    solver = Solver(board)

    if not solver.is_solvable():
        print("Board does not have solutions")
    else:
        print(f"Minimal number of steps {solver.moves()}")
        for board in solver.solution():
            print(board)


if __name__ == "__main__":
    main()
