import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_num = random.randint(1, 30)
    second_num = random.randint(1, 100)

    valid_answer = str(get_gcd(first_num, second_num))
    return f"{first_num} {second_num}", valid_answer


def get_gcd(a, b):
    if a < b:
        a, b = b, a

    remainder = b

    while remainder > 0:
        remainder = a % b
        answer, a, b = b, b, remainder

    return answer
