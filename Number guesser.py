import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize the number of guesses to 0
num_guesses = 0

# Loop until the player guesses the correct number
while True:
    # Prompt the player to guess the number
    guess = int(input("Guess a number between 1 and 100: "))

    # Increase the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", num_guesses, "guesses!")
        break

    # If the guess is incorrect, give a hint
    elif guess < number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
