#Rock Paper Scissors game
import random
no_rounds=int(input("How many Rounds? "))

   #declare win counters
comp_wins=0
user_wins=0
round_counter=1

while round_counter<=no_rounds:
    user_choice=input("Enter your Choice (R-Rock, P-Paper, S-Scissors ").upper()
    choices=["R","P","S"]
    comp_choice=random.choice(choices)
    print("Your Choice is ",user_choice)
    print("Computer Choice is ",comp_choice)

    if user_choice == comp_choice:
      print(f"Both players selected {user_choice}. It's a tie!")
      #No change in scores
    elif user_choice == "R":
        if comp_choice == "S":
           print("Rock smashes scissors! You win!")
           user_wins+=1
        else:
            print("Paper covers rock! You lose.")
            comp_wins+=1
    elif user_choice == "P":
        if comp_choice == "R":
           print("Paper covers rock! You win!")
           user_wins+=1
        else:
            print("Scissors cuts paper! You lose.")
            comp_wins+=1
    elif user_choice == "S":
        if comp_choice == "P":
           print("Scissors cuts paper! You win!")
           user_wins+=1
        else:
            print("Rock smashes scissors! You lose.")
            comp_wins+=1

    print("\n")
    print("computer wins ",comp_wins)
    print("user wins ",user_wins)
    # check for early game end
    if user_wins > no_rounds / 2 or comp_wins > no_rounds / 2:
        break
    round_counter+=1


print("\n")
if comp_wins>user_wins:
    print("Computer Won")
elif comp_wins<user_wins:
    print("You Won")
else: print("Its a Tie")
