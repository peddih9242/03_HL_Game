# 03 Number Checker, checks for valid numbers


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

# Main routine

the_check = num_check("Choose a number between 1 and 10: ", 1, 10)
print("program continues")