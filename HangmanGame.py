import random

# Predefined word list
guess_elements = ['omen', 'python', 'visual', 'game', 'computer']
lives = 6
guess_word = random.choice(guess_elements)
guess_list = ['_'] * len(guess_word)
guessed_letters = set()

print("Welcome to Hangman!")
print("The word to guess has", len(guess_word), "letters.")
print(" ".join(guess_list))

while lives > 0:
    print(f"\nYou have {lives} lives left.")
    guess_letter = input("Guess a letter: ").lower()

    # Input validation
    if not guess_letter.isalpha() or len(guess_letter) != 1:
        print("Invalid input. Please enter a single alphabet letter.")
        continue

    if guess_letter in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.add(guess_letter)

    if guess_letter in guess_word:
        print("Good guess!")

        for i, letter in enumerate(guess_word):
            if letter == guess_letter:
                guess_list[i] = guess_letter
    else:
        print("Wrong guess!")
        lives -= 1

    print(" ".join(guess_list))

    if '_' not in guess_list:
        print("\n🎉 Congratulations! You guessed the word:", guess_word)
        break

if lives == 0:
    print("\n😢 You lost! The word was:", guess_word)