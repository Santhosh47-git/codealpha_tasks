import random

words = ["apple", "grape", "mango", "berry", "melon"]

word = random.choice(words)


blanks = []
for i in range(len(word)):
    blanks.append("_")

turns = 6

print("Let's play Hangman!")

while turns > 0:
    print("\n" + " ".join(blanks))
    print("Turns left: " + str(turns)) 
    
    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                blanks[i] = guess
    else:
        print("Wrong!")
        turns = turns - 1 
  
    if "_" not in blanks:
        print("\n" + " ".join(blanks))
        print("You won! The word was " + word)
        break
        
    if turns == 0:
        print("\nGame Over. The word was " + word)
