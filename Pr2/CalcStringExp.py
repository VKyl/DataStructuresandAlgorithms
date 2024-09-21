from typing import Callable


class CalcStringExp:
    def __init__(self, expression: str):
        self.__expression = expression
        self.__operands: list[str] = []
        self.__operations: list[Callable] = []
        self.__last_is_number: bool = False
        self.__result: float = 0

        self.__OPERATORS: dict[str, Callable] = {
            '+': self.__add,
            '-': self.__sub,
            '*': self.__multiply,
            '/': self.__divide,
            '^': self.__pow,
        }

        self.__solve_expression()

    @property
    def result(self) -> float:
        return self.__result

    @staticmethod
    def __operation(function):
        def wrapper(self, *args):
            result = str(function(*args))
            self.__operands.append(result)

        return wrapper

    def __solve_expression(self):
        for char in self.__expression:
            self.__push(char)
        self.__result = self.__operands[0]

    def __push(self, char: str):
        if char == '(':
            self.__last_is_number = False
            return
        if char == ')':
            self.__calc()
            self.__last_is_number = False
            return
        if char.isdigit():
            if self.__last_is_number:
                self.__operands[-1] = self.__operands[-1] + char
            else:
                self.__last_is_number = True
                self.__operands.append(char)
            return

        self.__last_is_number = False
        self.__operations.append(self.__OPERATORS[char])

    def __calc(self):
        number2 = float(self.__operands.pop())
        number1 = float(self.__operands.pop())
        self.__operations.pop()(self, number1, number2)

    @__operation
    def __add(self, number1: float, number2: float):
        return number1 + number2

    @__operation
    def __sub(self, number1: float, number2: float):
        return number1 - number2

    @__operation
    def __multiply(self, number1: float, number2: float):
        return number1 * number2

    @__operation
    def __divide(self, number1: float, number2: float):
        if number2:
            return number1 / number2
        return 0

    @__operation
    def __pow(self, number1: float, number2: float):
        return number1 ** number2

    def __str__(self):
        return f'{self.__expression} = {self.__result}'


if __name__ == '__main__':
    calc1 = CalcStringExp('(1-(2+(4^2)))')
    calc2 = CalcStringExp('(1+((2+3)*(4*5)))')
    print(calc1)
    print(calc2)
