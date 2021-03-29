# String Checker


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

# Main Routine

yes_no_list = ["yes", "no"]

# loop for testing purposes
loop = ""
while loop == "":
    instructions = string_check("Would you like to see the instructions? ", yes_no_list, "Please enter yes or no.")
    # make sure that the program is getting the input we want it to
    if instructions == "yes" or "y":
        print("instructions")
    else:
        print("You said no")