import random
from typing import List

GAME_RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    initial_term = random.randint(1, 30)
    difference = random.randint(1, 10)
    length = 10

    progression = get_progression(initial_term, difference, length)

    skip_t = random.randint(0, len(progression) - 1)
    valid_answer = str(progression[skip_t])

    question = stringify(progression, skip_t)

    return question, valid_answer


def get_progression(initial_term, difference, length):

    progression = []

    for i in range(length):
        progression.append(initial_term + i * difference)

    return progression


def stringify(progression: List[int], hidden_term_index: int) -> str:

    for i in range(len(progression)):
        if i == hidden_term_index:
            progression[i] = ".."
        else:
            progression[i] = str(progression[i])

    return " ".join(progression)
