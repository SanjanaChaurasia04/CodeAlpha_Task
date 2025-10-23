#Q1.Hangman game 

import random
#List of predefined words
words=["apple","mango","banana","grapes","orange"]

#Randomly select a word
word=random.choice(words)
guessed_letters=[]
attempts=6

print("Welcome to hangman Game!")
print("_"*len(word))

#Game loop
while attempts>0:
    guess=input("Guess a letter: ").lower()

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter only one letter!!")
        continue
    if guess in guessed_letters:
        print("You have already guessed that letter!")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Good work! the letter is in the word.")
    else:
        attempts-=1
        print("Wrong guess! You have",attempts ,"attempts left.")

    #Show the curren guessed word
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter+ ""
        else:
            display+="_ "
    print(display)

    #Check if the player guessed all letters
    if "_" not in display:
        print("CONGRATULATIONS! YOU GUESSED THE WORD: ",word)
        break
    else:
        print("SORRY! YOU RAN OUT OF ATTEMPTS. THE WORD WAS: ",word)

