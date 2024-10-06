
from board import Board
import heapq


class Solver:
    def __init__(self, board):
        self._initial_board: Board = board

    def is_solvable(self):
        blocks: list[int] = self._initial_board.blocks.copy()

        inversions = 0
        for i in range(len(blocks)):
            for j in range(i + 1, len(blocks)):
                if blocks[i] and blocks[j] and blocks[i] > blocks[j]:
                    inversions += 1

        return not inversions % 2

    def moves(self) -> int:
        moves = len(self.solution()) - 1
        return moves

    @staticmethod
    def _solve(min_pq, current_board):
        visited = []
        came_from = {current_board: None}
        visited.append(current_board)

        while not current_board.is_goal():
            options = current_board.neighbors()

            for option in options:
                if option not in visited:
                    heapq.heappush(min_pq, option)
                    visited.append(option)
                    came_from[option] = current_board

            current_board = heapq.heappop(min_pq)

        path = []
        while current_board is not None:
            path.insert(0, current_board)
            current_board = came_from[current_board]

        return path

    def solution(self) -> list:
        min_pq = []
        current_board: Board = self._initial_board
        result = self._solve(min_pq, current_board)
        return result


def read_board_data(path) -> tuple[int, list[int]]:
    try:
        with open(path, 'r') as file:
            dimensions = int(file.readline())
            board = []
            for line in file.readlines():
                board.extend(map(int, line.split()))
        return dimensions, board
    except FileNotFoundError:
        print('File not found')


def main():
    data = read_board_data('./PazlTestFiles/puzzle3x3-unsolvable.txt')
    board = Board(*data)
    solver = Solver(board)

    if not solver.is_solvable():
        print("Board does not have solutions")
    else:
        print(f"Minimal number of steps {solver.moves()}")
        for board in solver.solution():
            print(board)


if __name__ == "__main__":
    main()
