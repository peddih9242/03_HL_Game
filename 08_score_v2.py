# Score component, shows score

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
guess = True
rounds = 2
game_summary = []
guess_question = "Please choose a number between {} and {}: ".format(lower, higher)
round_loop = 0
while round_loop != rounds:
    guess_total = 0
    round_loop += 1
    secret = random.randint(lower, higher)
    print(secret)
    valid = False
    while not valid:
        # ask guess question
        guess = num_check(guess_question, lower, higher)
        guess_total += 1
        # compare guess with the secret number
        if guess == secret:
            print("You won")
            result = "Round {}: Won with {} guesses.".format(round_loop, guess_total)
            # store summary per round in list
            game_summary.append(result)
            valid = True
        elif guess_total == 5:
            print("You lost")
            result = "Round {}: Lost with {} guesses.".format(round_loop, guess_total)
            game_summary.append(result)
            valid = True
        elif guess > secret:
            print("Lower")
        elif guess < secret:
            print("Higher")
# print the summary
print("Game Summary")
for item in game_summary:
    print(item)
