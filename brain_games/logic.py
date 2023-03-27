import prompt

COUNT_OF_QUESTIONS = 3


def start_to_game(module_of_game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(module_of_game.RULES_OF_GAME)

    for _ in range(COUNT_OF_QUESTIONS):
        task, correct_answer = module_of_game.create_task()
        print(f'Question: {task}')
        player_answer = input('Your answer: ')

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {player_name}!")
            return

    print(f'Congratulations, {player_name}!')
