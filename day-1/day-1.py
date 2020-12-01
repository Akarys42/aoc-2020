from typing import Tuple


def solution_1(data: str) -> int:
    data = parse_data(data)

    for i1, elem1 in enumerate(data):
        for elem2 in data[i1 + 1:]:
            if elem1 + elem2 == 2020:
                return elem1 * elem2


def solution_2(data: str) -> int:
    data = parse_data(data)

    for i1, elem1 in enumerate(data):
        for i2, elem2 in enumerate(data[i1 + 1:]):
            for elem3 in data[i2 + 1:]:
                if elem1 + elem2 + elem3 == 2020:
                    return elem1 * elem2 * elem3


def parse_data(data: str) -> Tuple[int]:
    return tuple(int(line) for line in data.split('\n'))
