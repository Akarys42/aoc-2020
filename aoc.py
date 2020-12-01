"""
Main dispatch script.
"""

import json
import sys

from typing import Tuple, Optional

USAGE = """\nUsage:\n\taoc.py [day] [environment]"""

VALID_ENVIRONMENTS = ('sample', 'challenge')


def main():
    if len(sys.argv) < 3:
        print(f'Not enough arguments supplied.{USAGE}')
        exit(1)

    try:
        day = int(sys.argv[1])
    except ValueError:
        print(f'{sys.argv[1]} isn\'t a valid number.{USAGE}')
        exit(1)

    environment = sys.argv[2]
    if environment not in VALID_ENVIRONMENTS:
        print(f'{environment} isn\'t a valid environment.\nAccepted values: {", ".join(VALID_ENVIRONMENTS)}.{USAGE}')

    print('Running solution...')
    solution, valid_solution = run_solution(day, environment)

    print(f'Solution found: {solution}')

    if valid_solution:
        if solution == valid_solution:
            print('Solution is valid!')
        else:
            print(f'Solution is invalid. The solution was {valid_solution}')


def run_solution(day: int, environment: str) -> Tuple[int, Optional[int]]:
    with open(f'./day-{day}/data.json') as f:
        json_data = json.load(f)

    data = json_data[environment]['data']
    if 'solution' in json_data[environment]:
        valid_solution = json_data[environment]['solution']
    else:
        valid_solution = None

    solution_handle = __import__(f'day-{day}.solution').solution

    return solution_handle(data), valid_solution


if __name__ == '__main__':
    main()
