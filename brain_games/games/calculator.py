import random

FIRST_NUMBER_RANGE = (11, 20)
SECOND_NUMBER_RANGE = (1, 10)


def get_brain_game_init_question():
    return 'What is the result of the expression?'


def get_question():
    operators = ("+", "-", "*")
    op = random.choice(operators)
    first_num = random.randint(FIRST_NUMBER_RANGE[0], FIRST_NUMBER_RANGE[1])
    second_num = random.randint(SECOND_NUMBER_RANGE[0], SECOND_NUMBER_RANGE[1])

    match op:
        case "*":
            return f"{first_num} * {second_num}", str(first_num * second_num)
        case "-":
            return f"{first_num} - {second_num}", str(first_num - second_num)
        case _:
            return f"{first_num} + {second_num}", str(first_num + second_num)
