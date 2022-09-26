import random

# set balance for testing purposes

STARTING_BALANCE = 10

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0, 20):
    chosen = random.randint(1, 100)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance += 1
    else:
        balance -= 0.5


print()
print("Starting Balance: ${:.2f}".format(5))
print("Final Balance: ${:.2f}".format(STARTING_BALANCE))
