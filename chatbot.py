"""
=========================================================
        CodeAlpha Smart Assistant
        Python Internship Project
=========================================================
"""

from datetime import datetime
import random
import time

# -------------------------------
# Project Information
# -------------------------------
BOT_NAME = "CodeAlpha Smart Assistant"
VERSION = "5.0"
DEVELOPER = "Navya"

# -------------------------------
# Data
# -------------------------------
quotes = [
    "Believe in yourself!",
    "Dream big and work hard.",
    "Success comes through consistency.",
    "Never stop learning.",
    "Every expert was once a beginner."
]

facts = [
    "Python was created by Guido van Rossum.",
    "The first computer programmer was Ada Lovelace.",
    "Artificial Intelligence is changing the world.",
    "Python is one of the most popular programming languages."
]

jokes = [
    "Why do programmers prefer Python? Because it's easy to read! 😂",
    "Debugging: Being the detective in a crime movie where you're also the criminal. 😄",
    "Why don't programmers like nature? It has too many bugs! 🐛"
]

# -------------------------------
# Session Variables
# -------------------------------
command_count = 0
start_time = datetime.now()

# -------------------------------
# Chat History
# -------------------------------
history = open("chat_history.txt", "a", encoding="utf-8")


def save_chat(user, bot):
    history.write(f"\n[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}]\n")
    history.write(f"User : {user}\n")
    history.write(f"Bot  : {bot}\n")


# -------------------------------
# Banner
# -------------------------------
def banner():
    print("=" * 60)
    print("🤖        CODEALPHA SMART ASSISTANT")
    print(" " * 18 + f"Version {VERSION}")
    print("=" * 60)


# -------------------------------
# Login
# -------------------------------
def login():
    while True:
        name = input("👤 Enter your name: ").strip()

        if name != "":
            return name

        print("❌ Name cannot be empty.")


# -------------------------------
# Bot Reply
# -------------------------------
def bot_reply(message):
    print("\nBot is typing...", end="")
    time.sleep(1)
    print("\r🤖 Bot:", message)


# -------------------------------
# Help Menu
# -------------------------------
def help_menu():
    print("\n" + "=" * 60)
    print("AVAILABLE COMMANDS")
    print("=" * 60)

    print("hello")
    print("how are you")
    print("date")
    print("time")
    print("quote")
    print("fact")
    print("joke")
    print("mood")
    print("calculator")
    print("game")
    print("about")
    print("help")
    print("bye")

    print("=" * 60)


# -------------------------------
# About
# -------------------------------
def about():
    print("\nProject   :", BOT_NAME)
    print("Version   :", VERSION)
    print("Developer :", DEVELOPER)
    print("Language  : Python")


# -------------------------------
# Calculator
# -------------------------------
def calculator():

    try:

        num1 = float(input("First Number : "))
        op = input("Operator (+ - * /): ")
        num2 = float(input("Second Number: "))

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":

            if num2 == 0:
                print("Cannot divide by zero.")
                return

            result = num1 / num2

        else:
            print("Invalid operator.")
            return

        print("Result =", result)

    except ValueError:
        print("Please enter valid numbers.")


# -------------------------------
# Guess Number Game
# -------------------------------
def guessing_game():

    number = random.randint(1, 10)

    print("\nGuess a number between 1 and 10")

    while True:

        try:

            guess = int(input("Your Guess: "))

            if guess == number:
                print("🎉 Correct! You Win!")
                break

            elif guess < number:
                print("Too Low!")

            else:
                print("Too High!")

        except ValueError:
            print("Enter numbers only.")

# -------------------------------
# Main Program
# -------------------------------

def main():

    global command_count

    banner()

    username = login()

    print(f"\nHello {username}! 👋")
    print("Hope you are having a wonderful day!")

    print("\n📅 Date :", datetime.now().strftime("%d-%m-%Y"))
    print("⏰ Time :", datetime.now().strftime("%I:%M %p"))

    print("\nType 'help' to see all commands.")
    print("Type 'bye' to exit.")

    while True:

        user = input(f"\n{username}: ").strip().lower()

        command_count += 1

        if user in ["hello", "hi", "hey"]:
            bot = f"Hello {username}! 😊"
            bot_reply(bot)

        elif user == "how are you":
            bot = "I'm doing great! Thanks for asking."
            bot_reply(bot)

        elif user == "date":
            bot = datetime.now().strftime("%d-%m-%Y")
            bot_reply(bot)

        elif user == "time":
            bot = datetime.now().strftime("%I:%M:%S %p")
            bot_reply(bot)

        elif user == "quote":
            bot = random.choice(quotes)
            bot_reply(bot)

        elif user == "fact":
            bot = random.choice(facts)
            bot_reply(bot)

        elif user == "joke":
            bot = random.choice(jokes)
            bot_reply(bot)

        elif user == "mood":
            mood = input("😊 How are you feeling today? ").lower()

            if mood in ["happy", "good", "great"]:
                bot = "That's wonderful! Keep smiling. 😊"

            elif mood in ["sad", "upset"]:
                bot = "Don't worry. Better days are ahead. ❤️"

            else:
                bot = "Thank you for sharing your feelings."

            bot_reply(bot)

        elif user == "calculator":
            calculator()
            continue

        elif user == "game":
            guessing_game()
            continue

        elif user == "help":
            help_menu()
            continue

        elif user == "about":
            about()
            continue

        elif user == "bye":
            bot = f"Goodbye {username}! 👋"
            bot_reply(bot)
            save_chat(user, bot)
            break

        else:
            bot = "Sorry! I don't understand that command."
            bot_reply(bot)

        save_chat(user, bot)

    end_time = datetime.now()

    print("\n" + "=" * 60)
    print("SESSION SUMMARY")
    print("=" * 60)
    print("User Name     :", username)
    print("Commands Used :", command_count)
    print("Start Time    :", start_time.strftime("%I:%M:%S %p"))
    print("End Time      :", end_time.strftime("%I:%M:%S %p"))
    print("Duration      :", end_time - start_time)
    print("=" * 60)

    history.close()

    print("\n❤️ Thank you for using CodeAlpha Smart Assistant!")
    print("🌟 Have a wonderful day!")


if __name__ == "__main__":
    main()