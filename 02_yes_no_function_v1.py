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


# Main Routine goes here
show_instructions = yes_no("Have You Played This Game "
                           "Before")
print("You Choose {}".format(show_instructions))
print()
having_fun = yes_no ("Are You Having Fun?")
print("You Said {} To Having Fun".format(having_fun))
