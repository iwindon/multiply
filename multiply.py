import random
import threading

def multiplication_practice():
    wrong_answers = []

    while True:
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

        user_answer = input(f"What is {num1} * {num2}? ")

        timer.cancel()

        if timeout[0]:
            wrong_answers.append((num1, num2, product))
            continue

        if user_answer.lower() == 'quit':
            break

        if int(user_answer) == product:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {product}.")
            wrong_answers.append((num1, num2, product))

    print("\nQuestions you got wrong:")
    for num1, num2, product in wrong_answers:
        print(f"{num1} * {num2} = {product}")

if __name__ == "__main__":
    multiplication_practice()