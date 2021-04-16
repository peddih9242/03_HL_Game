# max guesses component - calculates the number of guesses that user should get depending on low and high

import math
# loop for testing purposes
for item in range(0, 6):
    # get low and high (use num_check function in base component)
    low = int(input("Low: "))
    high = int(input("High: "))
    # calculate range from low and high
    hl_range = high - low + 1
    # calculate the highest amount of guesses needed with the binary search strategy
    max_raw = math.log2(range)
    # round up and give an extra guess just in case the user makes a mistake
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))
