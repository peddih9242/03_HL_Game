# 01 HL Base Component 31/03/2021
import random
# Functions


def string_check(question, valid_list, error):
    valid = False
    while not valid:
        # Ask question
        response = input(question).lower()
        for item in valid_list:
            # iterates through the list to check for the first letter of an item
            if response == item[0] or response == item:
                return response
        # if no item is found then print an error
        else:
            print(error)


def num_check(question, low=None, high=None):
    chosen = ""
    if low is not None and high is not None:
        chosen = "both"
    if low is not None and high is None:
        chosen = "low"
    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))
            if chosen == "both":
                # if there is a low and high then check that response is between low and high (for guessing)
                if response < low or response > high:
                    print("Please enter an integer between {} and {}.".format(low, high))
                    continue
            # make sure high is above the lower boundary
            elif chosen == "low":
                if response < low:
                    print("Please enter a number above {}.".format(low))
                    continue
            return response
        # if the input is not a number, print error
        except ValueError:
            print("Please enter an integer")


def instructions():
    # prints instructions
    print("***** INSTRUCTIONS *****")
    print("Every round you will be asked to...")
    print("- Enter a 'low' and 'high' number to guess between. The computer will generate a secret number"
          "which will be the one you are trying to guess.")
    print("- The computer will calculate how many guesses "
          "you are allowed depending on the low and high number you choose")
    print("- Enter the number of rounds you want to play (or press <enter> for an infinite mode")
    print("- Guess the secret number")

# Main Routine

# set up valid lists
yes_no_list = ["yes", "no"]
game_summary = []


show_instructions = string_check("Have you played this game before? ", yes_no_list, "Please enter "
                                                                                    "yes or no (or y / n).")
if show_instructions == "no" or show_instructions == "n":
    instructions()
print()
# get higher + lower boundaries and # of rounds
lower = num_check("Choose your lower number: ")
higher = num_check("Choose your higher number: ", lower + 1)
rounds = num_check("Rounds: ", 1)
# setup amount of rounds played and guessed
round_loop = 0
guess = True
guesses = 0
while round_loop != rounds:
    already_guessed = []
    # get secret number
    round_loop += 1
    secret = random.randint(lower, higher)

    guess_loop = False
    while not guess_loop:
        guesses += 1
        guess_question = "Enter a number between {} and {}: ".format(lower, higher)
        guess = num_check(guess_question, lower, higher)
        if guess in already_guessed:
            print("You have already guessed that number! Please enter a different number.")
            continue
        already_guessed.append(guess)
        if guess > secret:
            print("Lower!")
        elif guess < secret:
            print("Higher!")
        elif guess == secret:
            print("You won.")
            print()
            guess_loop = True
