import brain_games.game_gears
module_gg = brain_games.game_gears             # it's module short name
# module_game. - this is a short name of the module being loaded,
# see it at the beginning of the declaration function "begin_to_game"


def begin_to_game(MODULE_GAME):
    count_of_questions = 3
    result_of_game = 'win'      # flag for congratulations

    module_gg.greetings()
    player_name = module_gg.ask_player_name()
    module_gg.display_the_rules(MODULE_GAME.RULES_OF_GAME)

    for _ in range(count_of_questions):
        task, correct_answer = MODULE_GAME.create_task()
        module_gg.ask_player_question(task)
        player_answer = module_gg.get_player_answer()
        module_gg.display_test_result(player_answer, correct_answer,
                                      player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        module_gg.congratulate(player_name)
