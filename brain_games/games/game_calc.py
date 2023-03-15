from random import choices, randint

RULES_OF_GAME = 'What is the result of the expression?'


def formulate_task():
    first_item = randint(1, 100)
    mathematical_operation = choices('+-*')

    match mathematical_operation[0]:
        case '+':
            second_item = randint(1, 100)
            correct_answer = first_item + second_item
        case '-':
            second_item = randint(1, 100)
            correct_answer = first_item - second_item
        case '*':
            second_item = randint(1, 10)
            correct_answer = first_item * second_item

    task = f'{first_item} {mathematical_operation[0]} {second_item}'

    return task, str(correct_answer)
