import brain_games.game_gears
module_gg = brain_games.game_gears             # it's module short name
# module_game. - this is a short name of the module being loaded,
# see it at the beginning of the declaration function "begin_to_game"


def begin_to_game(name_of_game):
    match name_of_game:
        case 'brain_even':
            import brain_games.games.game_even
            module_game = brain_games.games.game_even
        case 'brain_calc':
            import brain_games.games.game_calc
            module_game = brain_games.games.game_calc
        case 'brain_gcd':
            import brain_games.games.game_gcd
            module_game = brain_games.games.game_gcd
        case 'brain_progression':
            import brain_games.games.game_progression
            module_game = brain_games.games.game_progression
        case 'brain_prime':
            import brain_games.games.game_prime
            module_game = brain_games.games.game_prime

    count_of_questions = 3
    result_of_game = 'win'      # flag for congratulations

    module_gg.greetings()
    player_name = module_gg.ask_player_name()
    module_gg.display_the_rules(module_game.rules_of_game)

    for _ in range(count_of_questions):
        task, correct_answer = module_game.formulate_task()
        module_gg.ask_player_question(task)
        player_answer = module_gg.get_player_answer()
        module_gg.display_test_result(player_answer, correct_answer,
                                      player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        module_gg.congratulate(player_name)
