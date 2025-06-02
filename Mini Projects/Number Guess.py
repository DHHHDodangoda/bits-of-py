# Number Guessing Game
# This program allows the computer to guess a number that the user is thinking of
# The user provides feedback on whether the guess is too high, too low, or correct

def play_game():
    print("Think of a number between 1 and 100. I will try to guess it!\n")
    low = 1
    high = 100
    attempts = 0

    # Start the guessing loop
    while True:
        guess = (low + high) // 2
        attempts += 1

        # Provide feedback on the guess
        print(f"My guess is {guess}.\n")
        feedback = input("Is it (h)igher, (l)ower, or (c)orrect?\n ").strip().lower()
        if feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} tries.")
            break
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Please enter 'h', 'l', or 'c'.")

# play again
while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing!")
        break