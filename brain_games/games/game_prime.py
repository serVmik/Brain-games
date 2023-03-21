from random import randint

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
SMALLEST_VALUE_OF_NUMBER = 1
LARGEST_VALUE_OF_NUMBER = 100


def is_prime(number):
    if number == 1:
        return False

    for divider in range(2, round(number / 2) + 1):
        if number % divider == 0:
            return False

    return True


def create_task():
    task = randint(SMALLEST_VALUE_OF_NUMBER, LARGEST_VALUE_OF_NUMBER)
    answer = ('no', 'yes')[is_prime(task)]

    return task, answer
