import random
import threading
import os

from colorama import init, Fore, Style

init(autoreset=True)

def multiplication_practice():
    wrong_answers = []
    question_count = 0
    correct_count = 0
    wrong_count = 0

    # Read the high score from the file
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            high_score = int(file.read())
    else:
        high_score = 0

    # Ask the user for the difficulty level
    difficulty = input("Choose a difficulty level (easy, hard, expert) - Default is expert: ")
    if difficulty.lower() == 'easy':
        timeout_seconds = 30
    elif difficulty.lower() == 'hard':
        timeout_seconds = 15
    else:
        timeout_seconds = 5

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
    if correct_count > high_score:
        with open('high_score.txt', 'w') as file:
            file.write(str(correct_count))

    print("\nQuestions you got wrong:")
    for num1, num2, product in wrong_answers:
        print(f"{num1} * {num2} = {product}")

if __name__ == "__main__":
    multiplication_practice()