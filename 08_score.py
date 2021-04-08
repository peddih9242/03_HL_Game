import random

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
# set variables
lower = 1
higher = 100
guesses_left = 5
secret = random.randint(lower, higher)
guess_question = "Please choose a number between {} and {}: ".format(lower, higher)
while guess != secret and guesses_left >= 1:
    # ask to guess
    guess = num_check(guess_question, lower, higher)
    guesses_left -= 1

    if guesses_left >= 1:
        if guess > secret:
            print("Lower")
        elif guess < secret:
            print("Higher")
        elif guess == secret:
            print("You won")
