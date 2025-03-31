# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...

# Write a python code to read the file and store the words in the list

# Write a function to guess a word randomly from the list.

# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter. 
# Display  letters in the clue word that were guessed correctly. 

# Let say word is EVAPORATE

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.

# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.


# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.

import random

def get_list_of_words():
    file = open("words.txt", 'r')
    return file.readlines()

def get_random_word(list):
    return list[random.randint(0, len(list))]

def display(word_to_guess, guessed):
    for c in word_to_guess:
        if c not in guessed:
            print("_", end=" ")
        else:
            print(c, end=" ")
    print()

def play_hangman(words_list):

    total_chances = 6
    print("HANGMAN GAME - YOU GET 6 CHANCE TO GUESS THE WORD")

    word_to_guess = get_random_word(words_list)
    to_guess = set(word_to_guess)
    guessed = set()

    while True:
        print("Welcome to Hangman!")
        display(word_to_guess, guessed)
        user_guess = input("Guess your next letter: ")
        won = False

        if user_guess in guessed:
            print(f"You already guessed the letter - {user_guess}")

        elif user_guess not in to_guess:
            guessed.add(user_guess)
            total_chances -= 1

            if total_chances == 0:
                print("You lost!! the word was - ", word_to_guess)
                break

            print(f"Incurrect!")

        else:
            guessed.add(user_guess)
            won = True

            for letter in to_guess:
                if letter not in guessed:
                    won = False
                    break

        if (won):
            print(f" {word_to_guess} is correct. \n \n You Won!!\n")  
            break
        else:
            print(f"You have {total_chances} chances to guess.\n")

if __name__ == "__main__":
    words_list = get_list_of_words()
    play_hangman(words_list)