import random


brain_game_init_question = 'What number is missing in the progression?'


def get_question():

    progression = get_progression()
    skip_i = random.randint(0, len(progression) - 1)

    valid_answer = str(progression[skip_i])
    progression[skip_i] = ".."

    question = ""
    for i in range(len(progression)):
        question = question + str(progression[i]) + " "

    return question, valid_answer


def get_progression():
    start = random.randint(1, 30)
    increment = random.randint(1, 10)
    progression = []

    for i in range(10):
        progression.append(start + i * increment)

    return progression
