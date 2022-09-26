

# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please Answer yes/no")


def instructions():
    print("**** How To Play ****")
    print()
    print("The rules of the game goes here")
    print()
    return ""


# Main Routine goes here
show_instructions = yes_no("Have You Played This Game "
                           "Before")

if show_instructions == "no":
    instructions()

    print("Program continues")
