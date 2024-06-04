import random
import threading
import os

from colorama import init, Fore, Style

init(autoreset=True)

def display_times_tables():
    while True:
        try:
            num = int(input(f"{Fore.WHITE}{Style.BRIGHT}Which times table would you like to see {Fore.YELLOW}{Style.BRIGHT}(1-10){Fore.WHITE}{Style.BRIGHT}? "))
            if 1 <= num <= 10:
                break
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a number.")
            
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

def update_score(correct_count, wrong_count, high_score, wrong_answers):
    # Update the high score if the current score is higher
    if correct_count > high_score:
        with open('high_score.txt', 'w') as file:
            file.write(str(correct_count))

    print("\nQuestions you got wrong:")
    for num1, num2, answer in wrong_answers:
        print(f"{num1} / {num2} = {answer}")

def set_difficulty():
    # Ask the user for the difficulty level
    difficulty = input("Choose a difficulty level (easy, hard, expert) - Default is expert: ")
    if difficulty.lower() == 'easy':
        timeout_seconds = 30
    elif difficulty.lower() == 'hard':
        timeout_seconds = 15
    else:
        timeout_seconds = 5
    return timeout_seconds

def get_high_score():
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            high_score = int(file.read())
    else:
        high_score = 0
    return high_score

def division_practice():
    wrong_answers = []
    question_count = 0
    correct_count = 0
    wrong_count = 0

    # Read the high score from the file
    high_score = get_high_score()   

    # Ask the user for the difficulty level
    timeout_seconds = set_difficulty()

    while question_count < 50:
        print(f"\n{Fore.WHITE}{Style.BRIGHT}Question {question_count + 1} of 50")
        print(f"{Fore.GREEN}{Style.BRIGHT}Correct answers: {correct_count}")
        print(f"{Fore.RED}{Style.BRIGHT}Wrong answers: {wrong_count}")
        print(f"{Fore.BLUE}{Style.BRIGHT}High score: {high_score}")

        divisor = random.randint(1, 10)
        quotient = random.randint(1, 10)
        num1 = divisor * quotient
        num2 = divisor
       
        quotient = num1 / num2

        timeout = [False]
        def time_up():
            print("\nTime's up!")
            print(f"The correct answer was {quotient}.")
            timeout[0] = True

        timer = threading.Timer(timeout_seconds, time_up)
        timer.start()

        user_answer = input(f"{Fore.WHITE}{Style.BRIGHT}What is {num1} / {num2}? {Style.RESET_ALL}")

        timer.cancel()

        if timeout[0]:
            wrong_answers.append((num1, num2, quotient))
            question_count += 1
            wrong_count += 1
            continue

        if user_answer.lower() == 'quit':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break

        try:
            user_answer = float(user_answer)
            if user_answer < 0 or user_answer > 10:
                raise ValueError
        except ValueError:
            print("Invalid entry. Please enter a number from 0 to 10.")
            continue

        if user_answer == quotient:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong! The correct answer is {quotient}.")
            wrong_answers.append((num1, num2, quotient))
            wrong_count += 1

        question_count += 1

    update_score(correct_count, wrong_count, high_score, wrong_answers)

def multiplication_practice():
    wrong_answers = []
    question_count = 0
    correct_count = 0
    wrong_count = 0

    # Read the high score from the file
    high_score = get_high_score()

    # Ask the user for the difficulty level
    timeout_seconds = set_difficulty()

    while question_count < 50:
        print(f"\n{Fore.WHITE}{Style.BRIGHT}Question {question_count + 1} of 50")
        print(f"{Fore.GREEN}{Style.BRIGHT}Correct answers: {correct_count}")
        print(f"{Fore.RED}{Style.BRIGHT}Wrong answers: {wrong_count}")
        print(f"{Fore.BLUE}{Style.BRIGHT}High score: {high_score}")

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        product = num1 * num2

        timeout = [False]
        def time_up():
            print("\nTime's up!")
            print(f"The correct answer was {product}.")
            timeout[0] = True

        timer = threading.Timer(timeout_seconds, time_up)
        timer.start()

        user_answer = input(f"{Fore.WHITE}{Style.BRIGHT}What is {num1} * {num2}? {Style.RESET_ALL}")

        timer.cancel()

        if timeout[0]:
            wrong_answers.append((num1, num2, product))
            question_count += 1
            wrong_count += 1
            continue

        if user_answer.lower() == 'quit':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break

        try:
            user_answer = int(user_answer)
            if user_answer < 1 or user_answer > 100:
                raise ValueError
        except ValueError:
            print("Invalid entry. Please enter a number from 1 to 100.")
            continue

        if user_answer == product:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong! The correct answer is {product}.")
            wrong_answers.append((num1, num2, product))
            wrong_count += 1

        question_count += 1

    # Update the high score if the current score is higher
    update_score(correct_count, wrong_count, high_score, wrong_answers)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.YELLOW}{Style.BRIGHT}Welcome to the math quiz!")
    print(f"{Fore.WHITE}{Style.BRIGHT}You will be asked 50 questions. You can quit at any time by typing 'quit'."
          f"\nYou will have 5 to 30 seconds to answer each question based on your level you chose."
          f"\nIf you don't answer in time, the question will be marked as wrong."
          f"\nYou can choose the difficulty level by typing 'easy', 'hard', or 'expert'. The default is 'expert'."
          f"\nGood luck!")
    while True:
        choice = input(f"{Fore.WHITE}{Style.BRIGHT}Would you like to (r)eview the times tables, take a (m)ultiplication quiz, a (d)ivision quiz, or (q)uit? ")
        if choice.lower() == 'r':
            display_times_tables()
        elif choice.lower() == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            multiplication_practice()
            break
        elif choice.lower() == 'd':
            os.system('cls' if os.name == 'nt' else 'clear')
            division_practice()
            break
        elif choice.lower() == 'q':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid choice. Please enter 'r' to review the times tables, 'm' to take a multiplication quiz, 'd' to take a division quiz, or 'q' to quit.")