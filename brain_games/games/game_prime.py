from random import randint

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False

    for divider in range(2, round(number / 2) + 1):
        if number % divider == 0:
            return False

    return True


def create_task():
    RANGE_OF_NUMBER = 100
    number = randint(1, RANGE_OF_NUMBER)

    task = str(number)
    answer = ('no', 'yes')[is_prime(number)]

    return task, answer
