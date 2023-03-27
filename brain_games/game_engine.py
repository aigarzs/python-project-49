import prompt


ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")

    print(game.GAME_RULES)

    for i in range(ROUNDS_COUNT):
        question, valid_answer = game.get_question_and_answer()

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
