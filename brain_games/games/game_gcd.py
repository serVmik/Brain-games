from random import randint
from math import gcd

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'
MIN_VALUE_OF_NUMBER = 1
MAX_VALUE_OF_NUMBER = 100


def create_task():
    first_number = randint(MIN_VALUE_OF_NUMBER, MAX_VALUE_OF_NUMBER)
    second_number = randint(MIN_VALUE_OF_NUMBER, MAX_VALUE_OF_NUMBER)
    task = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))

    return task, correct_answer
