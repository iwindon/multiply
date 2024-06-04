import random
import threading
import os

from colorama import init, Fore, Style

init(autoreset=True)

# Function to display times tables
def display_times_tables():
    # Loop until valid input is received
    while True:
        try:
            # Ask user for the times table they want to see
            num = int(input(f"{Fore.WHITE}{Style.BRIGHT}Which times table would you like to see {Fore.YELLOW}{Style.BRIGHT}(1-10){Fore.WHITE}{Style.BRIGHT}? "))
            # Check if input is within valid range
            if 1 <= num <= 10:
                break
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a number.")
            
    # Print the times table
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

    # Wait for user to press enter before continuing
    input("\nPress enter to continue...")
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to update the score
def update_score(correct_count, wrong_count, high_score, wrong_answers):
    # Update the high score if the current score is higher
    if correct_count > high_score:
        with open('high_score.txt', 'w') as file:
            file.write(str(correct_count))

    # Print the questions the user got wrong
    print("\nQuestions you got wrong:")
    for num1, num2, answer in wrong_answers:
        print(f"{num1} / {num2} = {answer}")

# Function to set the difficulty level
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

# Function to get the high score
def get_high_score():
    # Read the high score from the file
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            high_score = int(file.read())
    else:
        high_score = 0
    return high_score

# Function for division practice
def division_practice():
    # Initialize variable values
    wrong_answers = []
    question_count = 0
    correct_count = 0
    wrong_count = 0

    # Read the high score from the file
    high_score = get_high_score()   

    # Ask the user for the difficulty level
    timeout_seconds = set_difficulty()

    # Loop for 50 questions
    while question_count < 50:
        # Display question and score information
        print(f"\n{Fore.WHITE}{Style.BRIGHT}Question {question_count + 1} of 50")
        print(f"{Fore.GREEN}{Style.BRIGHT}Correct answers: {correct_count}")
        print(f"{Fore.RED}{Style.BRIGHT}Wrong answers: {wrong_count}")
        print(f"{Fore.BLUE}{Style.BRIGHT}High score: {high_score}")

        # Generate random numbers for the question
        divisor = random.randint(1, 10)
        quotient = random.randint(1, 10)
        num1 = divisor * quotient
        num2 = divisor
       
        quotient = num1 / num2

        # Set up a timer for the question
        timeout = [False]
        def time_up():
            print("\nTime's up!")
            print(f"The correct answer was {quotient}.")
            timeout[0] = True

        timer = threading.Timer(timeout_seconds, time_up)
        timer.start()

        # Get the user's answer
        user_answer = input(f"{Fore.WHITE}{Style.BRIGHT}What is {num1} / {num2}? {Style.RESET_ALL}")

        timer.cancel()

        # Check if the user wants to quit
        if timeout[0]:
            wrong_answers.append((num1, num2, quotient))
            question_count += 1
            wrong_count += 1
            continue

        if user_answer.lower() == 'quit':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break

        # Check if the user's answer is valid
        try:
            user_answer = float(user_answer)
            if user_answer < 0 or user_answer > 10:
                raise ValueError
        except ValueError:
            print("Invalid entry. Please enter a number from 0 to 10.")
            continue

        # Check if the user's answer is correct
        if user_answer == quotient:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong! The correct answer is {quotient}.")
            wrong_answers.append((num1, num2, quotient))
            wrong_count += 1

        question_count += 1

    # Update the score
    update_score(correct_count, wrong_count, high_score, wrong_answers)

# Function for multiplication practice
def multiplication_practice():
    # Initialize variable values
    wrong_answers = []
    question_count = 0
    correct_count = 0
    wrong_count = 0

    # Read the high score from the file
    high_score = get_high_score()

    # Ask the user for the difficulty level
    timeout_seconds = set_difficulty()

    # Loop for 50 questions
    while question_count < 50:
        # Display question and score information
        print(f"\n{Fore.WHITE}{Style.BRIGHT}Question {question_count + 1} of 50")
        print(f"{Fore.GREEN}{Style.BRIGHT}Correct answers: {correct_count}")
        print(f"{Fore.RED}{Style.BRIGHT}Wrong answers: {wrong_count}")
        print(f"{Fore.BLUE}{Style.BRIGHT}High score: {high_score}")

        # Generate random numbers for the question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        product = num1 * num2

        # Set up a timer for the question
        timeout = [False]
        def time_up():
            print("\nTime's up!")
            print(f"The correct answer was {product}.")
            timeout[0] = True

        timer = threading.Timer(timeout_seconds, time_up)
        timer.start()

        # Get the user's answer
        user_answer = input(f"{Fore.WHITE}{Style.BRIGHT}What is {num1} * {num2}? {Style.RESET_ALL}")

        timer.cancel()

        # Check if the user wants to quit
        if timeout[0]:
            wrong_answers.append((num1, num2, product))
            question_count += 1
            wrong_count += 1
            continue

        if user_answer.lower() == 'quit':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break

        # Check if the user's answer is valid
        try:
            user_answer = int(user_answer)
            if user_answer < 1 or user_answer > 100:
                raise ValueError
        except ValueError:
            print("Invalid entry. Please enter a number from 1 to 100.")
            continue

        # Check if the user's answer is correct
        if user_answer == product:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong! The correct answer is {product}.")
            wrong_answers.append((num1, num2, product))
            wrong_count += 1

        question_count += 1

    # Update the score
    update_score(correct_count, wrong_count, high_score, wrong_answers)

# Main program
if __name__ == "__main__":
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print welcome message
    print(f"{Fore.YELLOW}{Style.BRIGHT}Welcome to the math quiz!")
    print(f"{Fore.WHITE}{Style.BRIGHT}You will be asked 50 questions. You can quit at any time by typing 'quit'."
          f"\nYou will have 5 to 30 seconds to answer each question based on your level you chose."
          f"\nIf you don't answer in time, the question will be marked as wrong."
          f"\nYou can choose the difficulty level by typing 'easy', 'hard', or 'expert'. The default is 'expert'."
          f"\nGood luck!")
    # Loop until user chooses to quit
    while True:
        print(f"{Fore.WHITE}{Style.BRIGHT}Choose an option:")
        choice = input(f"""
        (r) Review the times tables
        (m) Take a multiplication quiz
        (d) Take a division quiz
        (q) Quit
        \nEnter your choice: """)
        # Check user's choice
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