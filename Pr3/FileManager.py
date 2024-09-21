from Point import Point


class FileManager:
    def __init__(self, path: str):
        self.__dir_path = path

    @property
    def dir_path(self):
        return self.__dir_path

    def read(self, file_name: str) -> list[Point]:
        try:
            with open(f'{self.__dir_path}/{file_name}', 'r') as file:
                for line in file.readlines()[1:]:
                    if line.split():
                        x, y = line.split()
                        point = Point(int(x), int(y))
                        yield point

        except FileNotFoundError as e:
            print(e)

    def __str__(self):
        return f'Directory: {self.__dir_path}'
