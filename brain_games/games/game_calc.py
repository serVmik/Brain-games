from random import choices, randint

RULES_OF_GAME = 'What is the result of the expression?'
SMALLEST_OPERAND_VALUE = 1
LARGEST_OPERAND_VALUE = 100


def create_task():
    first_operand = randint(SMALLEST_OPERAND_VALUE, LARGEST_OPERAND_VALUE)
    second_operand = randint(SMALLEST_OPERAND_VALUE, LARGEST_OPERAND_VALUE)
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
