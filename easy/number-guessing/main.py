import random

lowest_num = 10
highest_num = 1000
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game.")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}")


while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(
                f"Please enter a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print(f"Too low, try again!")
        elif guess > answer:
            print(f"Too high, try again!")
        elif guess == answer:
            print(
                f"Congratulations, you found the number in {guesses} guesses!")
            is_running = False
    else:
        print("Invalid input. Please enter a number.")
        print(
            f"I'm thinking of a number between {lowest_num} and {highest_num}")
