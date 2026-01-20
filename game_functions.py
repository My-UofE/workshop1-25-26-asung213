import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    # Binary search is put into place where the number of searches is minimised the most
    # Middle index is taken then returned as the computer's guess
    middle = len(poss_values) // 2
    return poss_values[middle]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    answer = ""
    if current_val < next_val:
        answer = "h"
    else:
        answer = "l"
    
    if answer == user_input:
        return True
    else:
        return False


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    guess = False
    # Loops through each letter in word and compare it to the letter guessed 
    # If true then guess is changed to True
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter 
            guess = True
    # The user is then told if their guess was successful or not and guess is returned
    if guess == True:
        print("Well done! " + letter + " is in the word")
    else:
        print("Sorry, " + letter + " is not in the word")
    return guess
