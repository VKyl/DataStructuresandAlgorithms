from typing import Callable


def read_file(filename: str, path: str = None, parser: Callable = lambda x: x):
    with open(f'{path + "/" if path else ""}{filename}', 'r') as file:
        for line in file:
            yield parser(line)
