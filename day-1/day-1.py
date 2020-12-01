from typing import Tuple


def solution_1(data: str) -> int:
    data = parse_data(data)

    for i1, elem1 in enumerate(data):
        for elem2 in data[i1 + 1:]:
            if elem1 + elem2 == 2020:
                return elem1 * elem2


def parse_data(data: str) -> Tuple[int]:
    return tuple(int(line) for line in data.split('\n'))
