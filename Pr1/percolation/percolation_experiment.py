from percolation import Percolation


class PercolationExperiment:
    def __init__(self, n: int, t: int):
        """
        run T separate experiments with NxN matrix
        :param n: <int> number of rows and columns in matrix
        :param t: <int> number of experiments
        """
        self.__matrix_side: int = n
        self.__experiments_result: list[int] = []
        self.__experiments_amount: int = t

    def run_experiments(self):
        for _ in range(self.__experiments_amount):
            percolation = Percolation(self.__matrix_side)
            percolation.start()
            self.__experiments_result.append(
                percolation.opened_count / self.__matrix_side**2)
        print(self)

    def mean(self) -> float:
        return sum(self.__experiments_result) / self.__experiments_amount

    def std(self) -> float:
        return (sum(map(self._std_mapper, self.__experiments_result)) /
                (self.__experiments_amount - 1)) ** 0.5

    def _std_mapper(self, x) -> float:
        return (x - self.mean()) ** 2

    def confidence_interval(self) -> tuple[float, float]:
        mean = self.mean()
        std = self.std()
        confidence_const = (std*1.96) / self.__experiments_amount ** 0.5
        return (mean - confidence_const), (mean + confidence_const)

    def __str__(self):
        lower, higher = self.confidence_interval()
        return (f'Matrix size: {self.__matrix_side}x{self.__matrix_side}, '
                f'Experiments amount: {self.__experiments_amount} \n'
                f'Mean: {self.mean(): .5f},\n'
                f'Std: {self.std(): .5f},\n'
                f'Confidence interval: [{lower: .5f},{higher: .5f}]')


def main():
    """
    run experiments and compute mean, std, confidence interval.
    print results on screen in readable format.
    """
    experiment = PercolationExperiment(200, 100)
    experiment.run_experiments()


if __name__ == "__main__":
    main()
