import random,time

#Define the words in a tuple data structure
guess_words=("budget","project","holiday","tailor","garden","factory","Kenya")
#fix the number of chances and declare counter for number of player guesses
chances=int(10)
no_of_player_guess=0
#welcome the user
player_name=(input("Whats your name? "))
print(f"Welcome to the Game {player_name}. Hope you dont het HANGED!")

time.sleep(1)

#select word to guess at random
play_word=random.choice(guess_words)
#print(play_word) #helps evaluate the program

#start the game
play_flag=input("Do you want to play (Y for yes,N for no ").upper()
#play the game
if play_flag=="Y":
    char_guesses=""
    while chances > 0:

        # counts the number of times a user fails
        failed = 0

        # all characters from the input
        # word taking one at a time.
        for char in play_word:

            # check if character in played word matches with players guess
            if char in char_guesses:
                print(char, end=" ")
            else:
                print("_")
                # for char that did not match, increase failures by one
                failed += 1
        if failed == 0:
            # user will win the game if failure is 0
            print(f"{player_name.upper()}!, Wins!")
            # Display the right word
            print("The word is: ", play_word)
            break
        # if user has input the wrong character type, user gets another chance to enter the right one
        print()
        guess = input("guess a character:")
        # every input character will be stored in guesses
        char_guesses+= guess
        # check input with the character in played word
        if guess not in play_word:
            chances -= 1
            # if the character doesn’t match the word then “Wrong” will be displayed
            print("Wrong")
            # Show number of chances left for the user
            print("You have", + chances, 'more guesses')
            if chances == 0:
                print("You Loose")
else: print("Bye")
quit()