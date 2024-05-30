import random
import threading

from colorama import init, Fore, Style

init(autoreset=True)

def multiplication_practice():
    wrong_answers = []
    question_count = 0
    correct_count = 0
    wrong_count = 0

    while question_count < 50:
        print(f"\nQuestion {question_count + 1} of 50")
        print(f"Correct answers: {correct_count}")
        print(f"Wrong answers: {wrong_count}")

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        product = num1 * num2

        timeout = [False]
        def time_up():
            print("\nTime's up!")
            print(f"The correct answer was {product}.")
            timeout[0] = True

        timer = threading.Timer(10.0, time_up)
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

    print("\nQuestions you got wrong:")
    for num1, num2, product in wrong_answers:
        print(f"{num1} * {num2} = {product}")

if __name__ == "__main__":
    multiplication_practice()