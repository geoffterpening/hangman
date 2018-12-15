from illustrations import *
from word_list import word_list
import random

# -----------Variables------------

guessed_letters = []
play_again = "y"
guesses = 0
guess_limit = 6
word = ""
word_letters = []
guess_letter = ""

ill_list = [ill_0, ill_1, ill_2, ill_3, ill_4, ill_5, ill_6]
# ------------debug stuff---------------


# -------------Game loop----------------
while play_again == 'y':
    word = word_list[random.randrange(249)]
    word_letters = list(word)
    print("\n\n------------------")
    print("-----HANGMAN------")
    print("------------------\n\nYou know how this works already, just play the game!\n")
    input("Ready? press enter to continue...")
    # guessing loop
    while guesses < guess_limit:
        # ***************** below should be while word letters length is not 0************
        while len(word_letters) > 0:
            print(ill_list[guesses])
            # *******************put underscores with the letters guessed in the right spot**************
            print("You have " + str(guess_limit - guesses) + " guesses left")
            print("letters guessed: ")
            print(guessed_letters)
            guess_letter = input("Make a guess: ")
            if len(guess_letter) == 1:
                if guess_letter not in guessed_letters:
                    guessed_letters.append(guess_letter)
                    if guess_letter in word:
                        # debug stuff:
                        print(str(word)+"|||"+str(word_letters))
                        # /debug stuff
                        word_letters = list(word)
                        #
                        # I need to make the below better - it only kills the first iteration of that letter, needs to do all
                        #
                        word_letters.remove(guess_letter)
                        word = "".join(word_letters)
                        # debug stuff
                        print(str(word_letters)+"|||"+str(word))
                        # /debug stuff
                        print("You got it right! ")
                    else:
                        # debug stuff
                        print(str(word) + "|||" + str(word_letters))
                        # /debug stuff
                        guesses += 1
                        print("\n\nYou got it wrong")
                        break
                else:
                    print("you aleady guessed that")

            else:
                print("\nPlease guess one letter at a time...")
        # print(guess_letter)
    print(ill_list[guesses])
    if guesses >= guess_limit:
        print("\nYou win!")
    else:
        print("\nYou lose!")
    # play again
    while True:
        play_again = input("Play again? y/n: ")
        if play_again not in["y", "n"]:
            print("\nPlease give a yes or no response\n")
        else:
            break
print("\n\nGood day to you! Now off you fuck!")
input("\nPress any key to quit: ")# User input section

