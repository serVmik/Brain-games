from random import randint
from math import gcd

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def create_task():
    RANGE_OF_NUMBER = 100
    first_number, second_number = ((randint(1, RANGE_OF_NUMBER),
                                    randint(1, RANGE_OF_NUMBER)))

    task = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))

    return task, correct_answer
