# List of possible words for the game
words = ["Hello", "City", "Car", "Country", "Home", "Laptop", "Everyday", "Morning"]

while True:
    # Number of attempts
    attempts = 10

    # Game loop
    for i in range(1, attempts + 1):
        word = input("Enter a word: ").capitalize()
        if word in words:
            print(f"Congratulations! The word '{word}' is in the list. You guessed it in {i} tries.")
            break
        else:
            print("The word is not in the list. Try again.")
    else:
        print("You've failed. The maximum number of attempts has been reached.")

    # Replay feature
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thank you for playing!")
        break
