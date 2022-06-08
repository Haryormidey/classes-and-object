from ast import Break
from multiprocessing import RLock
import random

print("Welcome!\nStarting Rock Paper Scissors game")
print("Choices")
print("R = Rock")
print("P = Paper")
print("S = Scissors")


# user_action = input("Enter a choice (R,P,S): ")
possible_options = ["R", "P", "S"]
# computer_action = random.choice(possible_options)

def choose_option():
    user_action = input("Enter a choice (R,P,S): ")
    if user_action in ("R","r"):
        user_action = "Rock"
    elif user_action in ("P","p"):
        user_action = "Paper"
    elif user_action in ("S","s"):
        user_action = "Scissors"
    else:
        print("Error!, try again.")
        # choose_option()
    return user_action

def computer_option():
    computer_action = random.choice(possible_options)
    if computer_action == ("R"):
        computer_action = "Rock"
    elif computer_action == ("P"):
        computer_action = "Paper"
    else:
        computer_action = "Scissors"
    return computer_action


while True:
    print("")
    user_action = choose_option()
    computer_action = computer_option()
    # print("Player",  user_action, ": CPU", computer_action )
    
    if user_action == computer_action:
        print(f"Player ({user_action}), : CPU ({computer_action})" )
        print(f"Both players selected {user_action}. It's a tie")

    elif user_action == "Rock":
        print(f"Player ({user_action}), : CPU ({computer_action})" )
        if computer_action == "Scissors":
            print("Rock smashes scissors! Player wins!")
            break 
        else:
            print("Paper covers rock! CPU wins!")
            break

    elif user_action == "Paper":
        print(f"Player ({user_action}), : CPU ({computer_action})" )
        if computer_action == "Rock":
            print("Paper covers rock! Player wins!!")
            break
        else:
            print("Scissors cuts paper! CPU wins!")
            break

    elif user_action == "Scissors":
        print(f"Player ({user_action}), : CPU ({computer_action})" )
        if computer_action == "Paper":
            print("Scissors cuts paper! Player wins!")
            break
        else:
            print("Rock smashes scissors! CPU wins!")
            break



    


