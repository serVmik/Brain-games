#!/usr/bin/env python3
# file:brain_even.py
import brain_games.bg_module
my_module = brain_games.bg_module


def main():
    count_of_questions = 3
    result_of_game = 'win'

    my_module.greetings()
    player_name = my_module.ask_player_name()
    my_module.display_the_rules()

    for _ in range(count_of_questions):
        task, correct_answer = my_module.formulate_a_task()
        my_module.ask_player_question(task)
        player_answer = my_module.get_player_answer()
        my_module.display_test_result(player_answer, correct_answer,
                                      player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        my_module.congratulate(player_name)


if __name__ == '__main__':
    main()
