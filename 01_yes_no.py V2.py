
show_instructions = ""

while show_instructions.lower() != "xxx":
    # Ask user if they have played before
    show_instructions = input("Have you played Lucky Unicorn before?")

    # If yes, output "program continues"
    if show_instructions.lower() == "yes" or show_instructions == "Y":
        print("Program Continues")

    # If no output 'display instructions'
    elif show_instructions.lower() == "no" or show_instructions == "N":
        print("Display Instructions")

    else:
        print("Please enter yes or no")
