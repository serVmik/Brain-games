import brain_games.game_gears
MODULE_GEARS = brain_games.game_gears


# MODULE_GAME is the game module reference
# that the begin_to_game()function receives when it is called
def begin_to_game(MODULE_GAME):
    COUNT_OF_QUESTIONS = 3
    result_of_game = 'win'      # flag for congratulations

    MODULE_GEARS.greetings()
    player_name = MODULE_GEARS.ask_player_name()
    MODULE_GEARS.display_the_rules(MODULE_GAME.RULES_OF_GAME)

    for _ in range(COUNT_OF_QUESTIONS):
        task, correct_answer = MODULE_GAME.create_task()
        MODULE_GEARS.ask_player_question(task)
        player_answer = MODULE_GEARS.get_player_answer()
        MODULE_GEARS.display_test_result(player_answer, correct_answer,
                                         player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        MODULE_GEARS.congratulate(player_name)
