import random
def hangman():
    words = ["apple", "banana", "mango", "orange", "python"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman Game!")
    print("_ " * len(word))
    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. {attempts} attempts left.")
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(display.strip())
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word '{word}'.")
            break
    else:
        print(f"\nGame Over! The word was '{word}'.")
if __name__ == "__main__":
    hangman()
