#!usr/bin/env python3
import brain_games.game_logics
import brain_games.games.game_prime
MODULE_GAME = brain_games.games.game_prime


def main():
    brain_games.game_logics.begin_to_game(MODULE_GAME)


if __name__ == '__main__':
    main()
