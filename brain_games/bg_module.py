# file:bg_module.py
import prompt
from random import choices, randint


def greetings():
    print('Welcome to the Brain Games!')


def ask_player_name():
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def generate_random_number(number_max):
    return randint(1, number_max)


def formulate_task_brain_even():
    task = generate_random_number(100)
    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (task, correct_answer)


def formulate_task_brain_calc():
    first_item = generate_random_number(100)
    mathematical_operation = choices('+-*')
    match mathematical_operation[0]:
        case '+':
            second_item = generate_random_number(100)
            correct_answer = first_item + second_item
        case '-':
            second_item = generate_random_number(100)
            correct_answer = first_item - second_item
        case '*':
            second_item = generate_random_number(10)
            correct_answer = first_item * second_item
    task = f'{first_item} {mathematical_operation[0]} {second_item}'
    return task, str(correct_answer)


def display_the_rules(rules_of_game):
    print(rules_of_game)


def ask_player_question(task):
    print(f'Qyestion: {task}')


def get_player_answer():
    return input('Your answer: ')


def display_test_result(player_answer, correct_answer, name):
    if player_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{player_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


def congratulate(name):
    print(f'Congratulations, {name}!')


def begin_the_game(name_of_game, rules_of_game):
    count_of_questions = 3
    result_of_game = 'win'

    greetings()
    player_name = ask_player_name()
    display_the_rules(rules_of_game)

    for _ in range(count_of_questions):
        match name_of_game:
            case 'brain_even':
                task, correct_answer = formulate_task_brain_even()
            case 'brain_calc':
                task, correct_answer = formulate_task_brain_calc()
        ask_player_question(task)
        player_answer = get_player_answer()
        display_test_result(player_answer, correct_answer,
                            player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        congratulate(player_name)
