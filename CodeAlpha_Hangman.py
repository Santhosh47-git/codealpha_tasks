import random

# List of 5 words
words = ["apple", "grape", "mango", "berry", "melon"]

# Pick a random word
word = random.choice(words)

# Create the blanks list
blanks = []
for i in range(len(word)):
    blanks.append("_")

turns = 6

print("Let's play Hangman!")

while turns > 0:
    # Show current board
    print("\n" + " ".join(blanks))
    print("Turns left:", turns)
    
    # Get user input
    guess = input("Enter a letter: ").lower()
    
    if guess in word:
        print("Correct guess!")
        # Find where the letter is in the word and replace the blank
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        print("Wrong!")
        turns = turns - 1

    # Check if user won
    if "_" not in blanks:
        print("\n" + " ".join(blanks))
        print("You won! The word was " + word)
        break

# Check if user lost
if turns == 0:
    print("\nGame Over. The word was " + word)