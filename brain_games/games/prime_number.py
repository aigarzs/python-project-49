import random


brain_game_init_question = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def get_question():
    number = random.randint(1, 100)

    if is_prime_number(number):
        valid_answer = "yes"
    else:
        valid_answer = "no"

    return str(number), valid_answer


def is_prime_number(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True
