# Functions go here
def num_checker(question, low, high):

# Main routine go here

    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
            try:
                        # ask the question
                        response = int(input(question))
                        # if the amount is too low/too high give
                        if low < response <= high:
                         return response

                        # output an error
                        else:
                            print(error)

              except ValueError:
                            print(error)

# Main routine go here
how_much = num_checker("How much would you "
                       " like to play with?",0 ,10)
