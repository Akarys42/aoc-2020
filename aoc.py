#! /bin/env python
"""
Main dispatch script.
"""

import json
import sys

from typing import Tuple, Optional

USAGE = """\nUsage:\n\taoc.py [day-part] [environment]"""

VALID_ENVIRONMENTS = ('sample', 'challenge')


def main():
    if len(sys.argv) < 3:
        print(f'Not enough arguments supplied.{USAGE}')
        exit(1)

    try:
        parts = sys.argv[1].split('-')

        if len(parts) != 2:
            raise ValueError

        day = int(parts[0])
        part = int(parts[1])

        if part not in (1, 2):
            raise ValueError

    except ValueError:
        print(f'{sys.argv[1]} doesn\'t have the right format.{USAGE}')
        exit(1)

    environment = sys.argv[2]
    if environment not in VALID_ENVIRONMENTS:
        print(f'{environment} isn\'t a valid environment.\nAccepted values: {", ".join(VALID_ENVIRONMENTS)}.{USAGE}')
        exit(1)

    print('Running solution...')
    solution, valid_solution = run_solution(day, part, environment)

    print(f'Solution found: {solution}')

    if valid_solution:
        if solution == valid_solution:
            print('Solution is valid!')
        else:
            print(f'Solution is invalid. The solution was {valid_solution}')


def run_solution(day: int, part: int, environment: str) -> Tuple[int, Optional[int]]:
    with open(f'./day-{day}/data.json') as f:
        json_data = json.load(f)

    data = json_data[environment]['data']
    if 'solution' in json_data[environment]:
        valid_solution = int(json_data[environment]['solution'][part - 1])
    else:
        valid_solution = None

    solution_handle = getattr(getattr(__import__(f'day-{day}.day-{day}'), f'day-{day}'), f'solution_{part}')

    return solution_handle(data), valid_solution


if __name__ == '__main__':
    main()
