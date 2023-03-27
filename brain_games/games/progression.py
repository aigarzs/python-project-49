import random


GAME_RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    initial_term = random.randint(1, 30)
    difference = random.randint(1, 10)
    length = 10

    progression = get_progression(initial_term, difference, length)

    skip_t = random.randint(0, len(progression) - 1)
    valid_answer = progression[skip_t]
    progression[skip_t] = ".."

    question = get_progression_to_string(progression)

    return question, valid_answer


def get_progression(initial_term, difference, length):

    progression = []

    for i in range(length):
        progression.append(str(initial_term + i * difference))

    return progression


def get_progression_to_string(progression):
    return " ".join(progression)
