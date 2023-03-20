import random


PROGRESSION_LENGTH = 10
PROGRESSION_START_RANGE = (1, 31)
PROGRESSION_INCREMENT_RANGE = (1, 11)


def get_brain_game_init_question():
    return 'What number is missing in the progression?'


def get_question():
    start = random.randint(PROGRESSION_START_RANGE[0], PROGRESSION_START_RANGE[1])
    increment = random.randint(PROGRESSION_INCREMENT_RANGE[0], PROGRESSION_INCREMENT_RANGE[1])
    skip_i = random.randint(1, PROGRESSION_LENGTH)

    question = ""
    for i in range(1, PROGRESSION_LENGTH + 1):
        num = start + increment * i
        if i == skip_i:
            valid_answer = str(num)
            question = question + ".. "
        else:
            question = question + str(num) + " "

    return question, valid_answer
