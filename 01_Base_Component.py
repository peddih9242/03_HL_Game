# 01 Base Component 31/03/2021

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


def num_check(question, low, high):
    error = "Please enter an integer between {} and {}".format(low, high)
    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))
            # if the inputted number is above the maximum or below the minimum then print an error
            if low <= response <= high:
                return response
            else:
                print(error)
        # if the input is not a number, print error
        except ValueError:
            print(error)


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


show_instructions = string_check("Have you played this game before? ", yes_no_list, "Please enter yes or no.")
if show_instructions == "yes" or show_instructions == "y":
    instructions()