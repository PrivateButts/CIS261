import random


def setupGame():
    maxRange = int(input("Enter the limit: "))
    print("Guess a number between 1 and", maxRange, "\n")
    return random.randint(1, maxRange)


def promptForGuess():
    guess = int(input("Enter your guess: "))
    if guess == secretNumber:
        return True
    elif guess > secretNumber:
        print("Too high!\n")
    else:
        print("Too low!\n")
    return False


if __name__ == "__main__":
    print("Guess the number!")
    print("=" * 17)

    while True:
        secretNumber = setupGame()
        guessCount = 0
        while True:
            guessCount += 1
            if promptForGuess():
                print("\nYou guessed it in", guessCount, "guesses!")
                break
        if input("\nPlay again? (y/n): ").lower() != "y":
            break
