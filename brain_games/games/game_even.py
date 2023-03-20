from random import randint

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_task():
    RANGE_OF_NUMBER = 100
    task = randint(1, RANGE_OF_NUMBER)

    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(task), correct_answer
