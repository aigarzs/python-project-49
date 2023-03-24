import random


brain_game_init_question = 'What is the result of the expression?'


def get_question():
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
