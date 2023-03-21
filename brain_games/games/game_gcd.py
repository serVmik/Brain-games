from random import randint
from math import gcd

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'
SMALLEST_VALUE_OF_NUMBER = 1
LARGEST_VALUE_OF_NUMBER = 100


def create_task():
    RANGE_OF_NUMBER = 100
    first_number = randint(SMALLEST_VALUE_OF_NUMBER, LARGEST_VALUE_OF_NUMBER)
    second_number = randint(SMALLEST_VALUE_OF_NUMBER, LARGEST_VALUE_OF_NUMBER)
    task = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))

    return task, correct_answer
