import random

options = ("r", "p", "s")

running = True

while running:

    player = None

    computer = random.choice(options)

    while player not in options:
        player = input(
            "Enter a choice (rock (r),paper (p), scissors (s) ): ").lower()

    print(f"Computer = {computer}")
    print(f"Player = {player}")

    if player == computer:
        print("it is a tie")
    elif player == "r" and computer == 's':
        print("rock smashes scissors, you win!")
    elif player == "p" and computer == 'r':
        print("You win!")
    elif player == "s" and computer == 'p':
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing")
