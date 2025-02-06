import random

# ASCII art for the hangman stages
HANGMAN_ART = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "computer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(HANGMAN_ART[incorrect_guesses])
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            incorrect_guesses += 1
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            print(HANGMAN_ART[incorrect_guesses])
            if attempts == 0:
                print(f"Sorry, you lost! The word was '{word}'.")
                break
        else:
            print("Good guess!")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word!")
            break

if __name__ == "__main__":
    hangman()
