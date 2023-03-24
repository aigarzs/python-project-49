import random


brain_game_init_question = 'Find the greatest common divisor of given numbers.'


def get_question():
    first_num = random.randint(1, 30)
    second_num = random.randint(1, 100)

    valid_answer = get_gcd(first_num, second_num)
    return f"{first_num} {second_num}", str(valid_answer)


def get_gcd(first_num, second_num):
    for answer in range(first_num, 0, -1):
        if first_num % answer == 0 and second_num % answer == 0:
            return answer
