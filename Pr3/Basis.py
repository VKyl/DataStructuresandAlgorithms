class Basis:
    def __init__(self, e1: (int, int), e2: (int, int)):
        self.__e1: (int, int) = e1
        self.__e2: (int, int) = e2
        self.__t_matrix = self.__get_change_matrix()

    @property
    def e1(self):
        return self.__e1

    @property
    def e2(self):
        return self.__e2

    @property
    def t_matrix(self):
        return self.__t_matrix

    def __get_change_matrix(self) -> ((float, float), (float, float)):
        det = self.e1[0] * self.e2[1] - self.e2[0] * self.e1[1]

        return (self.e2[1]/det, -self.e1[1]/det), (-self.e2[0]/det, self.e1[0]/det)

    def to_basis(self, vector: (int, int)) -> (float, float):
        new_vector = (self.t_matrix[0][0] * vector[0] + self.t_matrix[1][0] * vector[1],
                      self.t_matrix[0][1] * vector[0] + self.t_matrix[1][1] * vector[1])
        return new_vector

    def __str__(self):
        return f"{self.t_matrix}\n {self.e1} {self.e2}"


if __name__ == '__main__':
    basis = Basis((-3, 3), (-3, -3))
    print(basis.to_basis((1, 1)))
