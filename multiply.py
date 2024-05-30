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
    difficulty = input("Choose a difficulty level (easy, medium, difficult): ")
    if difficulty.lower() == 'easy':
        timeout_seconds = 60
    elif difficulty.lower() == 'medium':
        timeout_seconds = 30
    else:
        timeout_seconds = 10

    while question_count < 50:
        print(f"\nQuestion {question_count + 1} of 50")
        print(f"Correct answers: {correct_count}")
        print(f"Wrong answers: {wrong_count}")
        print(f"High score: {high_score}")

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

        user_answer = input(f"{Fore.YELLOW}{Style.BRIGHT}What is {num1} * {num2}? {Style.RESET_ALL}")

        timer.cancel()

        if timeout[0]:
            wrong_answers.append((num1, num2, product))
            question_count += 1
            wrong_count += 1
            continue

        if user_answer.lower() == 'quit':
            break

        if int(user_answer) == product:
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