import random
import prompt

from brain_games import cli

NUMBER_START = 1
NUMBER_FINISH = 20
ITERATIONS = 3

def main():
    cli.welcome_user()
    name = cli.name
        
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(ITERATIONS):
        number = random.randint(NUMBER_START, NUMBER_FINISH)
        
        valid_answer = "no"
        if number % 2 == 0:
            valid_answer = "yes"

        answer = prompt.string("Question " + str(number) + "\nYour answer: ")
        
        if answer == valid_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;( .Correct answer was '{valid_answer}'.\nLet's try again, {name}!")
            break
            
    else:
        print(f"Congratulations, {name}!")
        
        
if __name__ == "__main__":
    main()
    