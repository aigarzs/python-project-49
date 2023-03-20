import random


FIRST_NUMBER_RANGE = (1, 30)
SECOND_NUMBER_RANGE = (1, 100)


def get_brain_game_init_question():
    return 'Find the greatest common divisor of given numbers.'


def get_question():
    first_num = random.randint(FIRST_NUMBER_RANGE[0], FIRST_NUMBER_RANGE[1])
    second_num = random.randint(SECOND_NUMBER_RANGE[0], SECOND_NUMBER_RANGE[1])

    for answer in range(first_num, 0, -1):
        if first_num % answer == 0 and second_num % answer == 0:
            valid_answer = str(answer)
            return f"{first_num} {second_num}", valid_answer
