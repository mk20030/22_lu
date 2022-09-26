
# Functions go here
# yes no function assesses input for yes/no answer
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
        print("**** How To Play ****\n")
        print("""Welcome to Lucky Unicorn, the cost is 1$ per round to
    play.
    If you get a Unicorn you win $5
    if you receive a Horse ir Zebra you win 50c.
    A Donkey gets you nothing
    Good Luck!\n""")
     return ""

    # assess number is valid and within range
    def int_check(question):
        error= "Please a whole number between 1 and 10"
        valid=False
        while not valid:
            try:
                response = 
