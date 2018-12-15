from illustrations import *
from word_list import word_list
import random

# -----------Variables------------

remaining_letters = ["a", "b", "c", "d", "e", "f", "g", "h",
                     "i", "j", "k", "l", "m", "n", "o", "p",
                     "q", "r", "s", "t", "u", "v", "w", "x",
                     "y", "z"]
play_again = "y"
guesses = 0
guess_limit = 6
word = word_list[random.randrange(249)]

# ------------debug stuff---------------


# -------------Game loop----------------
while play_again == 'y':
    print("\n\n------------------")
    print("-----HANGMAN------")
    print("------------------\n\nYou know how this works already, just play the game!\n")
    input("Ready? press enter to continue...")
    while True:
        print(print(ill_0))
        print("You have "+str(guess_limit-guesses)+" guesses left")
        input()


# User input section

