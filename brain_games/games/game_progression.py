from random import randint

RULES_OF_GAME = 'What number is missing in the progression?'
SMALLEST_VALUE_OF_NUMBER = 1
LARGEST_VALUE_OF_NUMBER = 20
RANGE_OF_STEP = 10
SHORTEST_PROGRESSION_LENGTH = 5
LONGEST_PROGRESSION_LENGTH = 10


def create_progression():
    first_number = randint(SMALLEST_VALUE_OF_NUMBER, LARGEST_VALUE_OF_NUMBER)
    step = randint(SMALLEST_VALUE_OF_NUMBER, RANGE_OF_STEP)
    length_of_progression = randint(SHORTEST_PROGRESSION_LENGTH,
                                    LONGEST_PROGRESSION_LENGTH)
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
