import random

def get_difficulty():
    print("Welcome to the Number Guessing Game!")
    print("Choose Difficulty Level:")
    print("1. Easy (10 guesses)")
    print("2. Medium (7 guesses)")
    print("3. Hard (5 guesses)")
      
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
        continue

        attempts += 1


def play_game():
    guesses_allowed = get_difficulty()
    secret_number = random.randint(1, 100)
    attempts = 0
    wrong_guesses = 0

while attempts < guesses_allowed:
        try:
            guess = int(input(f"Guess a number between 1 and 100 (Remaining: {guesses_allowed - attempts}): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess == secret_number:
            print(f" Congratulations! You guessed it in {attempts} attempts!")
            save_score(attempts)
            break
        elif guess < secret_number:
            print("Too Low! ")
        else:
            print("Too High! ")

        wrong_guesses += 1
        
         # Optional Hint after 3 wrong tries
        if wrong_guesses == 3:
            if secret_number % 2 == 0:
                print(" Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

else:
        print(f"Game Over! The correct number was {secret_number}")
