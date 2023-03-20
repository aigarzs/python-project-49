import prompt
from brain_games import cli


ITERATIONS = 3


def run(game_module):
    name = cli.welcome_user()

    print(game_module.get_brain_game_init_question())

    for i in range(ITERATIONS):
        question, valid_answer = game_module.get_question()

        answer = prompt.string("Question: " + question + "\nYour answer: ")
        if answer == valid_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{valid_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
