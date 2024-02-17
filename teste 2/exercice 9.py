import random   

def guessing_game():
    secret_number = random.randint(1, 99)
    attempts = 0

    print("Welcome to the Guessing Game ")
    print("Try to guess the secret number between 1 and 99. Type 'exit' to quit.")

    while True:
        guess = input("Enter your guess: ")

        if guess.lower() == 'exit':
            print("Quitting the game...")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
            break

guessing_game()
