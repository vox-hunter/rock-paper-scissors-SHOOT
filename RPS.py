import random
import sys
# Getting user input
name = input("Welcome to ROCK! PAPER! SCISSORS! SHOOT!!\nEnter your name to start: ")
print("Be ready to lose", name)

choice = input("Enter your choice r/p/s: ").lower()

# Declaring r,p and s
if choice == "r":
    choice = "Rock"
    print("You chose", choice)
elif choice == "p":
    choice = "Paper"
    print("You chose", choice)
elif choice == "s":
    choice = "Scissors"
    print("You chose", choice)
else:
    print("Invalid input bro xD")
    sys.exit()
    
# Declaring boolean
draw = False
player_wins = False
player_loses = False

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    computer_choice = "Rock"
    print("I chose Rock")
elif computer_choice == 1:
    computer_choice = "Paper"
    print("I chose Paper")
elif computer_choice == 2:
    computer_choice = "Scissors"
    print("I chose Scissors")
else:
    print("Internal Error. Please try again")
    sys.exit()

if computer_choice == "Rock" and choice == "Rock":
    draw = True
elif computer_choice == "Rock" and choice == "Paper":
    player_wins = True
elif computer_choice == "Rock" and choice == "Scissors":
    player_loses = True
elif computer_choice == "Paper" and choice == "Rock":
    player_loses = True
elif computer_choice == "Paper" and choice == "Paper":
    draw = True
elif computer_choice == "Paper" and choice == "Scissors":
    player_wins = True
elif computer_choice == "Scissors" and choice == "Rock":
    player_wins = True
elif computer_choice == "Scissors" and choice == "Paper":
    player_loses = True
elif computer_choice == "Scissors" and choice == "Scissors":
    draw = True

if draw:
    print("It's a draw!")
elif player_wins:
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!")


