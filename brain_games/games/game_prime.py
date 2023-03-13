# file:game_prime.py
from random import randint


def formulate_task():
    number = randint(1, 10)
    answer = 'yes'

    task = str(number)

    if number == 1:
        answer = 'no'
        return task, answer

    for divider in range(2, round(number / 2) + 1):
        if number % divider == 0:
            answer = 'no'

    return task, answer
