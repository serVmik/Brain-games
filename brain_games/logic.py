from brain_games import gears

COUNT_OF_QUESTIONS = 3


def start_to_game(game_module):
    result_of_game = 'win'      # flag for congratulations
    gears.greetings()
    player_name = gears.ask_player_name()
    gears.display_the_rules(game_module.RULES_OF_GAME)

    for _ in range(COUNT_OF_QUESTIONS):
        task, correct_answer = game_module.create_task()
        gears.ask_player_question(task)
        player_answer = gears.get_player_answer()
        gears.display_test_result(player_answer, correct_answer, player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        gears.congratulate(player_name)
