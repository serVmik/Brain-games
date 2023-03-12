# file:brain_gsd.py
from random import randint

rules_of_game = 'Find the greatest common divisor of given numbers.'


def formulate_task():
    lower_number, largest_number = sorted((randint(1, 100), randint(1, 100)))

    for greatest_common_divisor in range(lower_number, 0, -1):
        if lower_number % greatest_common_divisor == 0 and\
           largest_number % greatest_common_divisor == 0:
            break

    task = f'{lower_number} {largest_number}'
    correct_answer = str(greatest_common_divisor)

    return task, correct_answer
