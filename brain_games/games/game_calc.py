from random import choices, randint

RULES_OF_GAME = 'What is the result of the expression?'


def create_task():
    RANGE_OF_FIRST_OPERAND = 100
    RANGE_OF_SECOND_OPERAND = 100
    first_operand = randint(1, RANGE_OF_FIRST_OPERAND)
    second_operand = randint(1, RANGE_OF_SECOND_OPERAND)
    mathematical_operation = choices(['+', '-', '*'])

    match mathematical_operation[0]:
        case '+':
            correct_answer = first_operand + second_operand
        case '-':
            correct_answer = first_operand - second_operand
        case '*':
            correct_answer = first_operand * second_operand

    task = f'{first_operand} {mathematical_operation[0]} {second_operand}'

    return task, str(correct_answer)
