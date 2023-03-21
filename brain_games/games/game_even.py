from random import randint

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
SMALLEST_VALUE_OF_NUMBER = 1
LARGEST_VALUE_OF_NUMBER = 100


def create_task():
    task = randint(SMALLEST_VALUE_OF_NUMBER, LARGEST_VALUE_OF_NUMBER)

    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(task), correct_answer
