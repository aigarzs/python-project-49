import random


GAME_RULES = 'What is the result of the expression?'


def get_question_and_answer():
    operators = ("+", "-", "*")
    op = random.choice(operators)
    first_num = random.randint(11, 20)
    second_num = random.randint(1, 10)

    match op:
        case "*":
            return f"{first_num} * {second_num}", str(first_num * second_num)
        case "-":
            return f"{first_num} - {second_num}", str(first_num - second_num)
        case "+":
            return f"{first_num} + {second_num}", str(first_num + second_num)
