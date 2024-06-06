"""
This script is a math quiz game where the user can practice multiplication, 
division, addition, and subtraction. 
The game includes features such as a times table review, a high score system, 
and adjustable difficulty levels.
"""
import random
import threading
import os
import operator

from colorama import init, Fore, Style

init(autoreset=True)

# Function to display times tables
def display_times_tables():
    """
    This function displays the times table of the number the user chooses.
    """
    # Loop until valid input is received
    while True:
        try:
            # Ask user for the times table they want to see
            num = int(input(f"{Fore.WHITE}{Style.BRIGHT}Which times table would you like to see"
                            f" {Fore.YELLOW}{Style.BRIGHT}(1-10){Fore.WHITE}{Style.BRIGHT}? "))
            # Check if input is within valid range
            if 1 <= num <= 10:
                break
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a "
                      f"number between 1 and 10.")
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
def update_score(correct_count, wrong_count, high_score, wrong_answers, operation_symbol):
    """
    This function updates the high score and displays the user's score.
    """
    # Update the high score if the current score is higher
    if correct_count > high_score:
        with open('high_score.txt', 'w') as file:
            file.write(str(correct_count))

    # Print the questions the user got wrong
    print(f"\n{Fore.WHITE}{Style.BRIGHT}You got {correct_count} questions correct "
          f"and {wrong_count} questions wrong.")
    print("\nQuestions you got wrong:")
    for num1, num2, answer in wrong_answers:
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    input("\nPress enter to continue...")
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to set the difficulty level
def set_difficulty():
    """
    This function asks the user to choose a difficulty level and returns the timeout in seconds.
    """
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
    """
    This function reads the high score from the file and returns it.
    """
    # Read the high score from the file
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r', encoding="utf-8") as file:
            high_score = int(file.read())
    else:
        high_score = 0
    return high_score

# Function for division practice
def generate_division_question():
    """
    This function generates a division question and returns the numbers and the quotient.
    """
    divisor = random.randint(1, 10)
    quotient = random.randint(1, 10)
    num1 = divisor * quotient
    num2 = divisor
    quotient = num1 / num2
    return num1, num2, quotient

# Function for multiplication practice
def generate_multiplication_question():
    """
    This function generates a multiplication question and returns the numbers and the product.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    product = num1 * num2
    return num1, num2, product

# Function for addition practice
def generate_addition_question():
    """
    This function generates an addition question and returns the numbers and the sum.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sum = num1 + num2
    return num1, num2, sum

def generate_subtraction_question():
    """
    This function generates a subtraction question and returns the numbers and the difference.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # Arrange num1 and num2 in descending order
    num1, num2 = max(num1, num2), min(num1, num2)
    difference = num1 - num2
    return num1, num2, difference

# Function to generate a question and get the user's answer
def get_user_answer(num1, num2, operation_symbol, operation, timeout_seconds):
    """
    This function generates a question and gets the user's answer.
    """
    timeout = [False]
    def time_up():
        print("\nTime's up!")
        print(f"The correct answer was {operation(num1, num2)}.")
        timeout[0] = True

    timer = threading.Timer(timeout_seconds, time_up)
    timer.start()

    user_answer = input(f"{Fore.WHITE}{Style.BRIGHT}What is {num1} {operation_symbol} "
                        f"{num2}? {Style.RESET_ALL}")

    timer.cancel()
    return user_answer, timeout[0]

# Function to check the user's answer
def check_answer(user_answer, correct_answer, answer_type):
    """
    This function checks the user's answer and returns whether it is correct or not.
    """
    try:
        user_answer = answer_type(user_answer)
        if user_answer < 0 or user_answer > 100:
            raise ValueError
    except ValueError:
        print("Invalid entry. Please enter a number from 0 to 100.")
        return False, True

    if user_answer == correct_answer:
        print("Correct!")
        return True, False
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
        return False, False

# Function to practice division
def division_practice():
    """
    This function practices division.
    """
    practice(generate_division_question, operator.truediv, float)

# Function to practice multiplication
def multiplication_practice():
    """
    This function practices multiplication.
    """
    practice(generate_multiplication_question, operator.mul, int)

# Function to practice addition
def addition_practice():
    """
    This function practices addition.
    """
    practice(generate_addition_question, operator.add, int)

# Function to practice subtraction
def subtraction_practice():
    """
    This function practices subtraction.
    """
    practice(generate_subtraction_question, operator.sub, int)

# Function to practice multiplication or division
def practice(generate_question, operation, answer_type):
    """
    This function practices multiplication or division.
    """
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
        # 
        num1, num2, correct_answer = generate_question()
        # Get the user's answer
        if operation == operator.mul:
            operation_symbol = 'x'
        elif operation == operator.truediv:
            operation_symbol = '/'
        elif operation == operator.add:
            operation_symbol = '+'
        elif operation == operator.sub:
            operation_symbol = '-'
        user_answer, timeout = get_user_answer(num1, num2, operation_symbol, operation, timeout_seconds)

        if timeout:
            wrong_answers.append((num1, num2, correct_answer))
            question_count += 1
            wrong_count += 1
            continue

        if user_answer.lower() == 'quit':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break

        correct, invalid = check_answer(user_answer, correct_answer, answer_type)
        if invalid:
            continue

        if correct:
            correct_count += 1
        else:
            wrong_answers.append((num1, num2, correct_answer))
            wrong_count += 1

        question_count += 1

    # Update the score
    update_score(correct_count, wrong_count, high_score, wrong_answers, operation_symbol)

# Main program
if __name__ == "__main__":
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print welcome message
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}{'*' * 57}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{'*' * 15} Welcome to the math quiz! {'*' * 15}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{'*' * 57}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}You will be asked 50 questions. You can quit at any time by typing 'quit'."
          f"\nYou will have 5 to 30 seconds to answer each question based on your level you chose."
          f"\nIf you don't answer in time, the question will be marked as wrong."
          f"\nYou can choose the difficulty level by typing 'easy', 'hard', or 'expert'."
          f" The default is 'expert'."
          f"\nGood luck!")
    # Loop until user chooses to quit
    while True:
        print(f"{Fore.WHITE}{Style.BRIGHT}Choose an option:")
        choice = input("""
        (r) Review the times tables
        (m) Take a multiplication quiz
        (d) Take a division quiz
        (a) Take a addition quiz
        (s) Take a subtraction quiz
        (q) Quit
        \nEnter your choice: """)
        # Check user's choice
        if choice.lower() == 'r':
            display_times_tables()
        elif choice.lower() == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            practice(generate_multiplication_question, operator.mul, int)
            
        elif choice.lower() == 'd':
            os.system('cls' if os.name == 'nt' else 'clear')
            practice(generate_division_question, operator.truediv, float)
            
        elif choice.lower() == 'a':
            os.system('cls' if os.name == 'nt' else 'clear')
            practice(generate_addition_question, operator.add, int)
            
        elif choice.lower() == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            practice(generate_subtraction_question, operator.sub, int)
            
        elif choice.lower() == 'q':
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            break
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid choice. Please try again.")