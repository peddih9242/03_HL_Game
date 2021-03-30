# 04 Guess Comparison, compares guess with the secret number


# checks for valid number
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

# set the secret number to 52
secret = 52

# loop for testing purposes (loops infinitely not based on rounds)
loop = ""
while loop == "":

    guess = num_check("Enter a number between 1 and 100 to guess: ", 1, 100)

    '''if guess is bigger than secret, say lower, if smaller than secret, print higher. win
     if they guess the secret number'''

    if guess > secret:
        print("Lower!")
    elif guess < secret:
        print("Higher!")
    elif guess == secret:
        print("You won.")
        loop = ","
