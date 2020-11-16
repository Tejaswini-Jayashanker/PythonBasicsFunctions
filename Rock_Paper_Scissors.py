''' This is a Python Program to Play Rock Paper Scissors.
Only one user can play against the computer.
'''
#Module Imports
import random

#Function Definitions
def print_menu():
	print("Enter 1 to choose Rock")
	print("Enter 2 to choose Scissors")
	print("Enter 3 to choose Paper")
	return

#main code
player = 0
computer = 0
choice = True
print("WELCOME TO THE GAME OF VIRTUAL ROCK | PAPER | SCISSORS ")
while( choice ):
    print_menu()
    comp_choice = random.randint(1,3) #On random, the computer chooses an option
    menu_option = int(input("Enter your choice: ") ) #This is the user option

    if ( menu_option == comp_choice ):
        print("DRAW")
    else:
        if(menu_option == 1 and comp_choice == 2):
            print("You Win! Comp chose Scissors")
            player += 1
        elif (menu_option == 2 and comp_choice == 1):
            print("Yay! I won, I chose Rock!")
            computer += 1
        elif (menu_option == 2 and comp_choice == 3):
            print( "You Win! Comp chose Paper")
            player += 1
        elif (menu_option == 3 and comp_choice == 2):
            print("Yay! I won, I chose Scissors!")
            computer += 1
        elif( menu_option == 3 and comp_choice == 1):
            print("You Win! Comp chose Rock")
            player += 1
        elif( menu_option == 1 and comp_choice == 3):
            print("Yay! I won, I chose Paper!")
            computer += 1
        else:
            print("Enter a Valid choice!!!")
            continue
    print("------------------------------------------------------")
    print("                 Scores are                           ")
    print("Computer : ",computer)
    print("You : ", player)
    print("------------------------------------------------------")
    if(computer == 5):
        print("Computer Won the Game!Thank you for playing")
        break
    elif(player == 5):
        print("Congratualtions! You won the game. Thank you for playing")
        break
    else:
        choice = input("Do you want to play? (Y/N):")
        choice = choice.upper
        if(choice == "N"):
            choice = False
