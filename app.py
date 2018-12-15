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
correct_letters = ""

ill_list = [ill_0, ill_1, ill_2, ill_3, ill_4, ill_5, ill_6]
# ------------debug stuff---------------


# -------------Game loop----------------
while play_again == 'y':
    play_again = ""
    # ^ Reset play_again

    # Set up word
    grab_word = word_list[random.randrange(249)]
    word = grab_word
    # ^picks a word from list
    word_letters = list(word)
    # ^separates letters of the word into a list so we can mess with it
    correct_letters = "_" * len(grab_word)
    # ^sets correct_letters to _____ for below purposes

    # Intro stuff
    print("\n\n------------------")
    print("-----HANGMAN------")
    print("------------------\n\nYou know how this works already, just play the game!\n")
    input("Ready? press enter to continue...")

    # Guessing loop
    while guesses < guess_limit:
        while len(word_letters) > 0:
            print(ill_list[guesses])
            # *******************put underscores with the letters guessed in the right spot**************
            print("You have " + str(guess_limit - guesses) + " guesses left")

            if len(guessed_letters) != 0:
                print("letters guessed: "+str(guessed_letters))
                # print(guessed_letters)
            else:
                ""
            # debug stuff:
            print(str(word) + " ||| " + str(word_letters))
            # /debug stuff
            if len(guessed_letters) != 0:
                print(correct_letters)
                # print("test")
            else:
                print("_" * len(grab_word))

            guess_letter = input("Make a guess: ")
            if len(guess_letter) == 1:
                if guess_letter not in guessed_letters:
                    guessed_letters.append(guess_letter)
                    if guess_letter in word:

                        # ------core mechanic part-----
                        word_letters = list(word)
                        # ^ converts the game word into a list so we can drop bits from it
                        word_letters[:] = (letter for letter in word_letters if letter != guess_letter)
                        # ^Drops guessed letter from word_letters

                        # Make the updated _li_t in correct_letters-----------------------***

                        print("".join(correct_letters))
                        for letter in grab_word:
                            if letter in guess_letter:
                                letter = guess_letter
                            else:
                                ""
                        # ^drops all instances of guess_letter out of the word_letters list

                        word = "".join(word_letters)
                        # ^ joins it all back into a single shorter string

                        # debug stuff
                        print(str(word_letters)+"   |||   "+str(word))
                        # /debug stuff

                        print("You got it right! ")
                    else:
                        # debug stuff
                        print(str(word) + "   |||   " + str(word_letters))
                        # /debug stuff
                        guesses += 1
                        print("\n\nYou got it wrong")
                        break
                else:
                    print("you already guessed that")

            else:
                print("\nPlease guess one letter at a time...")

    print(ill_list[guesses])
    if guesses <= guess_limit and len(word_letters) ==0:
        print("\nYou win!")
    else:
        print("\nYou lose!")
    # play again
    while True:
        play_again = input("Play again? y/n: ")
        if play_again not in["y", "n"]:

            # This makes the player lose LOL-----------------------------------------------*******
            print("\nPlease give a yes or no response\n")
        else:
            break
print("\n\nGood day to you! Now off you fuck!")
input("\nPress any key to quit: ")# User input section

