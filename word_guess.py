"""Word Guessing game using python's CLI. The Theme is common fruits you can
   find in any frocery store!"""
import random

all_words = ["apple", "orange", "strawberry", "grape", "raspberry",
             "kiwi", "pear", "grapefruit", "cranberry", "peach",
             "pineapple", "lemon", "lime", "cherry", "watermelon"]

def make_word_guess(word):
    """This function creates a list of dashes to substitute the word to guess"""
    dashes = []
    for dash in word:
        dash = "_"
        dashes.append(dash)
    return dashes

def end_game(word, puzzle, strikes):
    """Handles the game over conditions, victory and defeat"""
    if strikes < 1:
        try_again = input("Game over... Want to try again? 'Y' to try again, 'n' to quit:\n")
        if try_again.lower() == "y":
            game_start(all_words)
        elif try_again.lower() == "n":
            print("Goodbye!")
    if word == "".join(puzzle):
        you_win = input("You Guessed it! The word was " +
                        word.upper() +
                        "! Play again? 'Y' to start again, 'N' to quit:\n")
        if you_win.lower() == "y":
            game_start(all_words)
        elif you_win.lower() == "n":
            print("Goodbye!")

def user_turns(word, puzzle, strikes):
    """Handles how each turn is resolved (i.e. conditions for right and wrong guesses)"""
    while strikes > 0 and word != "".join(puzzle):
        print(" ".join(puzzle) + "\n")
        print("Guesses left: " + str(strikes))
        user_guess = input("Your Guess (letters only): ")
        if user_guess.isalpha() and len(user_guess) == 1:
            index_pos_list = []
            index_pos = 0
            print("You guessed '" + user_guess + "'")
            if word.find(user_guess.lower()) != -1:
                print("CORRECT!")
            else:
                print("UH OH, that letter was not found")
                strikes -= 1
                if strikes >= 1:
                    print("\nNEXT ROUND! Keep Guessing!\n")
            while True:
                try:
                    index_pos = word.index(user_guess, index_pos)
                    index_pos_list.append(index_pos)
                    index_pos += 1
                except ValueError:
                    break
            for letter_index in index_pos_list:
                puzzle[letter_index] = word[letter_index]
            #print(index_pos_list)

            #for x in word:
                #if x == user_guess.lower() and puzzle[word.index(x) != x]:
                    #puzzle[word.index(x)] = x
        elif user_guess.isalpha() and len(user_guess) > 1:
            print("one letter at a time, please!\nLet's try that again! Enter a letter to guess!\n")
        else:
            print("Only letters are accepted, no numbers, punctuation or symbols")
            print("Let's try that again! Enter a letter to guess!\n")
    end_game(word, puzzle, strikes)

def game_start(words):
    """Starts any new game, including when the program runs and when the player want
       to play again"""
    word_to_guess = random.choice(words)
    game_word = make_word_guess(word_to_guess)
    #strikes_left = 9
    print("\nWelcome to WORD GUESS: FRUIT EDITION!")
    print("*************************************")
    choose_diff = input("Choose your difficulty! ('Easy', 'Normal', or 'Hard'):\n")
    if choose_diff.lower() == 'easy':
        strikes_left = 9
    elif choose_diff.lower() == 'normal':
        strikes_left = 6
    elif choose_diff.lower() == 'hard':
        strikes_left = 3
    print("\nNow guess the fruit!\n")
    user_turns(word_to_guess, game_word, strikes_left)

game_start(all_words)
