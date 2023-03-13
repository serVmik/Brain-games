# file:game_gears.py
import prompt


def greetings():
    print('Welcome to the Brain Games!')


def ask_player_name():
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


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
              f"Correct answer was '{correct_answer}'."
              f"Let's try again, {name}!")


def congratulate(name):
    print(f'Congratulations, {name}!')
