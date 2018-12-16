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
    print("------------------\n\nPlay the game!\n")
    input("Ready? press enter to continue...")

    # Guessing loop
    while guesses < guess_limit and len(word_letters) != 0:
        while len(word_letters) > 0:
            print(ill_list[guesses]+"\n")
            # letters guessed
            if len(guessed_letters) != 0:
                print("letters guessed: " + ", ".join(guessed_letters))
                # print(guessed_letters)
                print("You have " + str(guess_limit - guesses) + " guesses left\n")
            else:
                ""

            if len(guessed_letters) != 0:
                print("Word: "+correct_letters)
                # print("test")
            else:
                print("Word: "+correct_letters)

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
                        count_num = 0
                        working_correct_letters = ""
                        for letter in correct_letters:
                            if grab_word[count_num] == guess_letter:
                                working_correct_letters = working_correct_letters+guess_letter
                            else:
                                working_correct_letters = working_correct_letters+correct_letters[count_num]
                            count_num += 1
                        correct_letters = working_correct_letters
                        # print("\n\nWord: "+correct_letters)
                        count_num = 0


                        word = "".join(word_letters)
                        # ^ joins it all back into a single shorter string

                        print("You got it right! ")
                        if len(word_letters) == 0:
                            break
                        else:
                            ""
                    else:
                        guesses += 1
                        print("\n\nYou got it wrong")
                        break
                else:
                    print("\n\nyou already guessed that...")

            else:
                print("\nPlease guess one letter at a time...")

    print(ill_list[guesses])
    if guesses <= guess_limit and len(word_letters) ==0:
        print("\nYou win!")
    else:
        print("\nYou lose!")
        print("The word you were looking for was "+"\""+grab_word+"\"\n")
    # play again
    while True:
        play_again = input("Play again? y/n: ")
        guesses = 0
        guessed_letters = []
        if play_again not in["y", "n"]:
            print("\nPlease give a yes or no response\n")
        else:
            break
print("\n\nGood day to you! Now off you fuck!")
input("\nPress any key to quit: ")# User input section

