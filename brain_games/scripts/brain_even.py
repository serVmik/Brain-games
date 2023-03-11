#!/usr/bin/env python3
# file:brain_even.py
import brain_games.bg_module
my_module = brain_games.bg_module


def main():
    name_of_game = 'brain_even'
    rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    my_module.begin_the_game(name_of_game, rules_of_game)


if __name__ == '__main__':
    main()
