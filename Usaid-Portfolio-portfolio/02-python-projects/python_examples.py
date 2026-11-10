# Beginner Python Projects
# Run this file with Python 3.

import random

def calculator():
    print("\nSIMPLE CALCULATOR")
    first = float(input("Enter first number: "))
    operator = input("Choose +, -, * or /: ")
    second = float(input("Enter second number: "))

    if operator == "+":
        print("Answer:", first + second)
    elif operator == "-":
        print("Answer:", first - second)
    elif operator == "*":
        print("Answer:", first * second)
    elif operator == "/":
        if second != 0:
            print("Answer:", first / second)
        else:
            print("You cannot divide by zero.")
    else:
        print("Unknown operator.")

def guessing_game():
    print("\nNUMBER GUESSING GAME")
    secret = random.randint(1, 10)
    guess = int(input("Guess a number from 1 to 10: "))
    if guess == secret:
        print("Correct! Great job.")
    else:
        print("Not quite. The number was", secret)

def mini_quiz():
    print("\nMINI QUIZ")
    score = 0
    answer = input("What does HTML stand for? ").strip().lower()
    if answer == "hypertext markup language":
        print("Correct!")
        score += 1
    else:
        print("The answer is HyperText Markup Language.")
    print("Your score:", score, "/ 1")

def temperature_converter():
    print("\nTEMPERATURE CONVERTER")
    celsius = float(input("Temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit:", fahrenheit)

while True:
    print("\n=== PYTHON PROJECTS MENU ===")
    print("1. Calculator")
    print("2. Guessing game")
    print("3. Mini quiz")
    print("4. Temperature converter")
    print("5. Exit")
    choice = input("Choose a project: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        guessing_game()
    elif choice == "3":
        mini_quiz()
    elif choice == "4":
        temperature_converter()
    elif choice == "5":
        print("Thanks for trying my projects!")
        break
    else:
        print("Please choose a number from 1 to 5.")
