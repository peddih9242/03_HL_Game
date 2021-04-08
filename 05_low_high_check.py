# 05 Low High check, checks that the user checks a lower number than the higher number when choosing low/high

import random
# Function


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

# main routine
game_summary = []
# set variables
lower = num_check("Choose your lower number: ")
higher = num_check("Choose your higher number: ", lower + 1)
rounds = num_check("Rounds: ", 1)
secret = random.randint(lower, higher)
print(secret)
guess_question = "Please choose a number between {} and {}: ".format(lower, higher)
guess = 0
while guess != secret:
    guess = num_check(guess_question, lower, higher)
