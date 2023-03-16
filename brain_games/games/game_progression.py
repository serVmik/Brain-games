from random import randint

RULES_OF_GAME = 'What number is missing in the progression?'


def create_progression():
    RANGE_OF_FIRST_NUMBER = 20
    RANGE_OF_STEP = 10
    PROGRESSION_LENGTH_RANGE = 10
    first_number = randint(1, RANGE_OF_FIRST_NUMBER)
    step = randint(1, RANGE_OF_STEP)
    length_of_progression = randint(5, PROGRESSION_LENGTH_RANGE)
    last_number = first_number + length_of_progression * step
    list_of_progression = [_ for _ in range(first_number, last_number, step)]

    return list_of_progression


def creat_task_and_answer(progression):
    position_of_hidden_element = randint(1, len(progression) - 1)
    hidden_element = progression[position_of_hidden_element]
    answer = str(hidden_element)

    task = ''
    progression[position_of_hidden_element] = '..'
    for element in progression:
        task += str(element) + ' '

    return task[:-1], answer


def create_task():
    progression = create_progression()
    task, correct_answer = creat_task_and_answer(progression)

    return task, correct_answer
