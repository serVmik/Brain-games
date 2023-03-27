from random import choice, randint

RULES_OF_GAME = 'What is the result of the expression?'
MIN_OPERAND_VALUE = 1
MAX_OPERAND_VALUE = 100


def create_task():
    first_operand = randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    second_operand = randint(MIN_OPERAND_VALUE, MAX_OPERAND_VALUE)
    mathematical_operation = choice(['+', '-', '*'])

    match mathematical_operation:
        case '+':
            correct_answer = first_operand + second_operand
        case '-':
            correct_answer = first_operand - second_operand
        case '*':
            correct_answer = first_operand * second_operand

    task = f'{first_operand} {mathematical_operation} {second_operand}'

    return task, str(correct_answer)
