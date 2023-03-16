from random import randint

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create_task():
    RANGE_OF_NUMBER = 100
    number = randint(1, RANGE_OF_NUMBER)
    answer = 'yes'

    task = str(number)

    if number == 1:
        answer = 'no'
        return task, answer

    for divider in range(2, round(number / 2) + 1):
        if number % divider == 0:
            answer = 'no'

    return task, answer
