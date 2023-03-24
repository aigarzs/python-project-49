import random


brain_game_init_question = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def get_question():
    number = random.randint(1, 20)

    if is_even_number(number):
        valid_answer = "yes"
    else:
        valid_answer = "no"

    return str(number), valid_answer


def is_even_number(num):
    return num % 2 == 0
