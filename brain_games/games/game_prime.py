from random import randint

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_VALUE_OF_NUMBER = 1
MAX_VALUE_OF_NUMBER = 100


def is_prime(number):
    if number == 1:
        return False

    for divider in range(2, round(number / 2) + 1):
        if number % divider == 0:
            return False

    return True


def create_task():
    task = randint(MIN_VALUE_OF_NUMBER, MAX_VALUE_OF_NUMBER)
    answer = ('no', 'yes')[is_prime(task)]

    return task, answer
