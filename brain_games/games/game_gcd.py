from random import randint

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def formulate_task():
    RANGE_OF_NUMBER = 100
    first_number, second_number = ((randint(1, RANGE_OF_NUMBER),
                                    randint(1, RANGE_OF_NUMBER)))
    lesser_number = min(first_number, second_number)

    for greatest_common_divisor in range(lesser_number, 0, -1):
        if first_number % greatest_common_divisor == 0 and\
           second_number % greatest_common_divisor == 0:
            break

    task = f'{first_number} {second_number}'
    correct_answer = str(greatest_common_divisor)

    return task, correct_answer
