import random
import logo_art

EASY_LEVEL = 12
MEDIUM_LEVEL = 10
HARD_LEVEL = 6

def set_difficulty(level_choosen):
    level_choosen = level_choosen.lower()
    if level_choosen == 'easy':
        return EASY_LEVEL
    elif level_choosen == 'medium':
        return MEDIUM_LEVEL
    elif level_choosen == 'hard':
        return HARD_LEVEL
    else:
        return None

def check_answer(guess_number, answer, attempts):
    if guess_number < answer:
        print("Your guess is too low")
        return attempts - 1
    elif guess_number > answer:
        print("Your guess is too high")
        return attempts - 1
    else:
        print(f"Your guess is right.... the answer is {answer}")
        return attempts

def game():
    print(logo_art.logo)
    print("Let's think of a number between 1 -- 50")
    answer = random.randint(1, 50)
    level = input("Choose difficulty level 'Easy' 'Medium' 'Hard': ")
    attempts = set_difficulty(level)
    if attempts is None:
        print("You entered wrong difficulty level")
        return
    guess_number = 0
    while guess_number != answer:
        print(f"You have {attempts} attempts remaining")
        guess_number = int(input("Guess a number: "))
        attempts = check_answer(guess_number, answer, attempts)
        if guess_number == answer:
            break
        if attempts == 0:
            print("You are out of guesses.... You lose")
            print(f"The correct answer was {answer}")
            break
        print("Guess again")

while True:
    game()
    choice = input("\nEnter 'play' to play again or 'exit' to quit: ").lower()
    if choice == "exit":
        print("Game exited")
        break