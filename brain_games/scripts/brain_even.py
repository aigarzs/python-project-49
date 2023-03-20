#!/usr/bin/env python3
from brain_games.games import even_number
from brain_games import game_engine


def main():
    game_engine.run(even_number)


if __name__ == "__main__":
    main()
