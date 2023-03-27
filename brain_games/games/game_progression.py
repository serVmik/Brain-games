from random import randint

RULES_OF_GAME = 'What number is missing in the progression?'
MIN_VALUE_OF_NUMBER = 1
MAX_VALUE_OF_NUMBER = 20
RANGE_OF_STEP = 10
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def create_progression(first_number, length, step):
    last_number_of_progression = first_number + step * (length - 1)
    list_of_progression = [
        str(number) for number in range(
            first_number, last_number_of_progression + 1, step)]

    return list_of_progression


def creat_task_and_answer(progression):
    position_of_hidden_element = randint(1, len(progression) - 1)
    hidden_element = progression[position_of_hidden_element]
    answer = hidden_element

    progression[position_of_hidden_element] = '..'
    task = ', '.join(progression)

    return task, answer


def create_task():
    first_number_of_progression = randint(
        MIN_VALUE_OF_NUMBER, MAX_VALUE_OF_NUMBER)
    length_of_progression = randint(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    step_of_progression = randint(
        MIN_VALUE_OF_NUMBER, RANGE_OF_STEP)
    progression = create_progression(
        first_number_of_progression, length_of_progression, step_of_progression)

    task, correct_answer = creat_task_and_answer(progression)

    return task, correct_answer
