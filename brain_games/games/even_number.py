import random


NUMBER_START = 1
NUMBER_FINISH = 20


def get_brain_game_init_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    number = random.randint(NUMBER_START, NUMBER_FINISH)

    valid_answer = "no"
    if number % 2 == 0:
        valid_answer = "yes"

    return str(number), valid_answer
