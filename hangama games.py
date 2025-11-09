import random

# 1. Setup: Predefined word list and game constants
WORD_LIST = ["python", "hangman", "coding", "challenge", "simple"]
MAX_INCORRECT_GUESSES = 6
HANGMAN_PICS = [
    # 0 incorrect guesses
    """
       +---+
           |
           |
           |
          ===
    """,
    # 1 incorrect guess
    """
       +---+
       O   |
           |
           |
          ===
    """,
    # 2 incorrect guesses
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    # 3 incorrect guesses
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    # 4 incorrect guesses
    """
       +---+
       O   |
      /|\\  |
           |
          ===
    """,
    # 5 incorrect guesses
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===
    """,
    # 6 incorrect guesses (Game Over)
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    """
]

def get_display_word(secret_word, guessed_letters):
    """Generates the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    """Main game function."""
    
    # Select a random word
    secret_word = random.choice(WORD_LIST).lower()
    
    # Initialize game state variables
    guessed_letters = set()
    incorrect_guesses = 0
    
    print("👋 Welcome to Simple Hangman!")
    print(f"The word has {len(secret_word)} letters. Start guessing!")
    
    # --- Main Game Loop ---
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        
        current_display = get_display_word(secret_word, guessed_letters)
        
        # Check for win condition
        if "_" not in current_display:
            print(f"\n🎉 Congratulations! You guessed the word: **{secret_word.upper()}**")
            break
            
        print("\n" + HANGMAN_PICS[incorrect_guesses])
        print(f"Word: **{current_display}**")
        print(f"Incorrect Guesses Left: **{MAX_INCORRECT_GUESSES - incorrect_guesses}**")
        print(f"Guessed Letters: {sorted(list(guessed_letters))}")
        print("-" * 30)

        # Get player input
        while True:
            try:
                guess = input("Enter a letter: ").lower()
                if len(guess) != 1 or not 'a' <= guess <= 'z':
                    print("Please enter a single, valid letter (a-z).")
                elif guess in guessed_letters:
                    print(f"You already guessed '{guess}'. Try a different letter.")
                else:
                    break # Valid guess received
            except EOFError:
                print("\nExiting game.")
                return

        guessed_letters.add(guess)

        # Check the guess
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is NOT in the word.")
            
    # --- Game Over ---
    else: # This 'else' block executes if the while loop finishes normally (i.e., incorrect_guesses >= MAX_INCORRECT_GUESSES)
        print("\n" + HANGMAN_PICS[MAX_INCORRECT_GUESSES])
        print("💀 Game Over!")
        print(f"The secret word was: **{secret_word.upper()}**")

# Start the game
if __name__ == "__main__":
    play_hangman()