"""  Please make sure you read the entire README.md file to follow the instructions. 
You dont have to follow how I have started the game. Please use your creativity """

#Ivy's and Branden's game
import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        guess = input("Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 10.")
            continue

        guess = int(guess)
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit loop when guessed correctly

    return attempts

# Main program loop
while True:
    play_game()
    
    # Ask if the user wants to play again
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! Goodbye.")
        break

