import random

wordList = ["ruby","javascript","kotlin","python","csharp"]
word = random.choice(wordList)
word_display = ["_" for letter in word]
print(word_display)
attempts = 8
print("Welcome to hangman")
while attempts>0 and "_" in word_display:
    print("\n"+" ".join(word_display))
    guess  = input("Guess a letter :").lower()
    if guess in word:
        for index,value in enumerate(word):
            if value==guess:
                word_display[index]= guess

    else:
        print("Not the correct guess")
        attempts-=1

if attempts<=0 and "_" in word_display:
    print("You lose, loser")
else:
    print(f"You guess in {attempts} attempts")