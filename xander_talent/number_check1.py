# create a function to guess computer number


def guess_computer_number():
    """This will keep asking the user to guess
    until they enter a matching number.
    """
    import random

    guess = int(input("Enter a number between 1 - 100: "))
    computer_number = random.randint(1, 100)
    match = guess == computer_number
    while not match:
        guess = int(input("Try again. Enter a number between 1 - 100: "))
        match = guess == computer_number
    else:
        print("You matched!")


guess_computer_number()
