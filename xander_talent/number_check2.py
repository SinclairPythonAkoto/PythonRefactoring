# create a function to guess computer number


def guess_computer_number():
    """This will give the user a num of attempts
    to guess the computers number.

    It also tells you how many attempts it took to match.
    """
    import random

    attempts = 0
    computer_number = random.randint(1, 100)
    while attempts < 4:
        guess = input("Guess the computer's number. Pick a number between 1 - 100: ")
        guess = int(guess)
        attempts += 1
        if guess == computer_number:
            break
        elif guess > computer_number:
            print("Too high!")
        elif guess < computer_number:
            print("Too low!")
    if guess == computer_number:
        print("You matched!")
        print(f"Attempts: {attempts}")


guess_computer_number()
