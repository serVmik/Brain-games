from random import randint

rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def formulate_task():
    task = randint(1, 100)
    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(task), correct_answer
