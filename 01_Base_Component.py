# 01 HL Base Component 31/03/2021
# TO DO - lower message and higher message use statement function

import random
import math

# Functions


# string function checks for a valid string or the first letter from a list
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


# checks user has entered an integer, optionally checks that
# integer is more than a  minimum / between two numbers
def num_check(question, low=None, high=None):
    chosen = ""
    # set situations
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


# outputs instructions on request, returns <blank>
def instructions():
    # prints instructions
    print()
    statement_gen("INSTRUCTIONS", "!")
    print()
    print("Every round you will be asked to...")
    print("- Enter a 'low' and 'high' number to guess between. The computer will generate a secret number"
          "which will be the one you are trying to guess.")
    print("- The computer will calculate how many guesses "
          "you are allowed depending on the low and high number you choose")
    print("- Enter the number of rounds you want to play (or press <enter> for an infinite mode")
    print("- Guess the secret number")


# decorates important messages, returns <blank>
def statement_gen(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    above = decoration * len(statement)
    print(above)
    print(statement)
    print(above)
    return ""

# Main Routine

# set up valid responses to display instructions
yes_no_list = ["yes", "no"]


# question to decide whether to show instructions
show_instructions = string_check("Have you played this game before? ", yes_no_list, "Please enter "                                   "yes or no (or y / n).")
if show_instructions == "no" or show_instructions == "n":
    instructions()
print()

# loop game section of program
keep_going = ""
while keep_going == "":

    # get higher + lower boundaries and # of rounds
    lower = num_check("Choose your lower number: ")
    higher = num_check("Choose your higher number: ", lower + 1)
    rounds = num_check("Rounds: ", 1)

    # calculate range from low and high
    hl_range = higher - lower + 1

    # calculate the highest amount of guesses needed with the binary search strategy
    max_raw = math.log2(hl_range)

    # round up and give an extra guess just in case the user makes a mistake
    max_upped = math.ceil(max_raw)
    guess_limit = max_upped + 1

    # setup variables that will be used in the game
    round_loop = 0
    guess = True
    best_score = higher + 1
    worst_score = lower - 1
    avg_sum = 0
    won = 0
    lost = 0

    while round_loop != rounds:
        already_guessed = []
        game_summary = []
        guesses = 0
        guess_left = guess_limit

        # calculate the highest amount of guesses needed with the binary search strategy
        max_raw = math.log2(hl_range)

        # round up and give an extra guess just in case the user makes a mistake
        max_upped = math.ceil(max_raw)
        guess_limit = max_upped + 1

        # get secret number
        round_loop += 1
        secret = random.randint(lower, higher)
        print(secret)

        # notify user if a new round has started
        if round_loop > 1:
            round_statement = "Round {} of {}: You have {} guesses".format(round_loop, rounds, guess_limit)
            statement_gen(round_statement, "#")
            print()
        while guess != secret:
            guesses += 1
            guess_left -= 1
            guess_question = "Enter a number between {} and {}: "\
                .format(lower, higher, guess_left)

            # ask for user to guess
            guess = num_check(guess_question, lower, higher)
            print()

            # if it is a duplicate guess, tell the user
            if guess in already_guessed:
                print("You have already guessed that number! Please enter a different number.")
                print()
                guess_left += 1
                guesses -= 1
                continue
            already_guessed.append(guess)

            # compare guess with secret to say lower, higher or to detect win/loss, get
            # the worst/best scores and guesses (and average amount of guesses)
            # to add to game summary for end of game statistics
            if guess == secret:
                result = "Round {}: {} guesses (won)".format(round_loop, guesses)
                if guesses == 1:
                    won_statement = "Amazing, you guessed the number in 1 try"
                else:
                    won_statement = "You guessed the number in {} guesses".format(guesses)
                statement_gen(won_statement, "!")
                game_summary.append(result)
                if guesses < best_score:
                    best_score = guesses
                if guesses > worst_score:
                    worst_score = guesses
                avg_sum = avg_sum + guesses
                won += 1
            elif guess_left <= 0:
                result = "Round {}: {} guesses (lost, ran out of guesses)".format(round_loop, guesses)
                lost_statement = "You ran out of guesses, the secret number was {}".format(secret)
                statement_gen(lost_statement, "!")
                game_summary.append(result)
                worst_score = guesses
                avg_sum = avg_sum + guesses
                if guesses < best_score:
                    best_score = guesses
                guess = secret
                lost += 1
            elif guess > secret:
                lower_statement = "Too high, try a lower number - guesses left: {}".format(guess_left)
                statement_gen(lower_statement, "^")
            elif guess < secret:
                higher_statement = "Too low, try a higher number - guesses left: {}".format(guess_left)
                statement_gen(higher_statement, "^")
            print()

    # game summary and statistics output
    avg_guess = avg_sum / rounds
    won_lost = "Won: {} | Lost: {}".format(won, lost)
    statement_gen(won_lost, "-")
    print()
    stats = input("Press <enter> if you would like to see your game statistics: ")
    if stats == "":
        print()
        statement_gen("Game Summary", "=")
        print()
        for item in game_summary:
            print(item)
        print()
        print("Best: {}".format(best_score))
        print("Worst: {}".format(worst_score))
        print("Average: {:.2f}".format(avg_guess))
        print()

    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
print("Thanks for playing")
