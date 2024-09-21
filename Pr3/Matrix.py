class Matrix:
    def __init__(self, cols: int, rows: int):
        self.__cols = cols
        self.__rows = rows
        self.__matrix = [[1] * cols] * rows

    @property
    def cols(self):
        return self.__cols

    @property
    def rows(self):
        return self.__rows

    @property
    def matrix(self):
        return self.__matrix.copy()

    @matrix.setter
    def matrix(self, new_matrix):
        self.__matrix = new_matrix.copy()

    def __mul__(self, other):
        try:
            result = []
           

            return result
        except IndexError:
            print("Wrong size")
        except TypeError:
            print("Not iterable")

    def copy(self):
        matrix_copy = Matrix(self.cols, self.rows)
        matrix_copy.matrix = self.matrix
        return matrix_copy

    def __str__(self):
        return str(self.__matrix)


if __name__ == '__main__':
    matrix = Matrix(2, 2)
    matrix2 = Matrix(1, 2)

    print(matrix * matrix2)
