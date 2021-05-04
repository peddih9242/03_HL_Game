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

# Main routine
# set variables
lower = 1
higher = 100
guess = True
rounds = 2
game_summary = []
guess_question = "Please choose a number between {} and {}: ".format(lower, higher)
round_loop = 0
rounds_won = 0
rounds_lost = 0
best_score = 101
worst_score = 0
avg = 0
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
            rounds_won += 1
            print("You won")
            result = "Round {}: Won with {} guesses.".format(round_loop, guess_total)
            # store summary per round in list
            game_summary.append(result)
            if guess_total < best_score:
                best_score = guess_total
            elif guess_total > worst_score:
                worst_score = guess_total
            avg = avg + guess_total
            valid = True
        # if there has been 5 guesses, show that the user lost
        elif guess_total == 5:
            worst_score = guess_total
            print("You lost")
            avg = avg + guess_total
            rounds_lost += 1
            result = "Round {}: Lost with {} guesses.".format(round_loop, guess_total)
            game_summary.append(result)
            valid = True
        # print higher/lower depending on situation
        elif guess > secret:
            print("Lower")
        elif guess < secret:
            print("Higher")
# print the summary
avg_score = avg / round_loop
print("*** Game Summary ***")
print()
print("Won: {}   |   Lost: {}".format(rounds_won, rounds_lost))
print()
for item in game_summary:
    print(item)
print()
print("Best Score: {}".format(best_score))
print("Worst Score: {}".format(worst_score))
print("Average: {:.2f}".format(avg_score))
