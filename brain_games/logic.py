from brain_games import gears

COUNT_OF_QUESTIONS = 3


def start_to_game(module_of_game):
    gears.greetings()
    player_name = gears.ask_player_name()
    gears.display_the_rules(module_of_game.RULES_OF_GAME)

    for _ in range(COUNT_OF_QUESTIONS):
        task, correct_answer = module_of_game.create_task()
        gears.ask_player_question(task)
        player_answer = gears.get_player_answer()
        gears.display_test_result(player_answer, correct_answer, player_name)

        if player_answer != correct_answer:
            return

    gears.congratulate(player_name)
