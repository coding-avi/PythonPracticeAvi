import random


def get_word():
    """Choose and return a random word from the word list"""
    words = ["hello", "what", "apple", "orange", "pink", "book", "stand", "cover", "button", "mango"]
    return random.choice(words)


def initialize_secret(word):
    """Create and return a secret display with underscores"""
    secret = ["_"] * len(word)
    return secret


def update_secret(word, secret, guess):
    """Update the secret display if the guessed character is in the word"""
    for i in range(len(word)):
        if word[i] == guess:
            secret[i] = guess
    return secret


def display_game(secret):
    """Display the current state of the secret"""
    print(secret)


def play_game():
    """Main game loop for hangman"""
    word = get_word()
    secret = initialize_secret(word)
    
    print("Welcome to Hangman!")
    display_game(secret)
    
    for attempt in range(10):
        guess = input(f"Attempt {attempt + 1}/10 - Please enter a guessing character: ")
        
        if guess in word:
            secret = update_secret(word, secret, guess)
        
        display_game(secret)
        if "_" not in secret:
            print("Congratulations! You've guessed the word!")
            break
    
    print("The word was:", word)


if __name__ == "__main__":
    play_game()