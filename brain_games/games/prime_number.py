import random

NUMBER_RANGE = (1, 100)
PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97)


def get_brain_game_init_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    number = random.randint(NUMBER_RANGE[0], NUMBER_RANGE[1])

    valid_answer = "no"
    for i in PRIME_NUMBERS:
        if i == number:
            valid_answer = "yes"
            break

    return str(number), valid_answer
