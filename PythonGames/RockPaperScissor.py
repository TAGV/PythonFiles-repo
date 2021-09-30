#Rock Paper Scissor game

import random
import sys

print("\t\tRocks Papers Scissorrrs....Game!!!\n")

wins,loss,tie = 0,0,0
print("Wins:",wins,"Loss:",loss,"Tie:",tie)
while True: #Loop for Whole game
    user = input("Enter Rock(r/R),Paper(p/P),Scissor(s/S),Quit(q/Q)\n")
    while True: #Loop for User Input
        if user.lower() == 'q':
            print("Game Over")
            print("Final Score = Wins:", wins, "Loss:", loss, "Tie:", tie)
            sys.exit() #Exit the Program
        elif user.lower() == 'r':
            print("User : Rock")
            break
        elif user.lower() == 'p':
            print("User : Paper")
            break
        elif user.lower() == 's':
            print("User : Scissor")
            break
        else:
            break


    machine = random.randint(1,3)
    if machine == 1:
        print("Machine : Rock")
    elif machine == 2:
        print("Machine : Paper")
    elif machine == 3:
        print("Machine : Scissor")

    if user.lower() == 'r' and machine == 1:
        print("Tie")
        tie = tie + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 'p' and machine == 2:
        print("Tie")
        tie = tie + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 's' and machine == 3:
        print("Tie")
        tie = tie + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

    if user.lower() == 'r' and machine == 2:
        print("User Lost")
        loss = loss + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 'r' and machine == 3:
        print("User Won")
        wins = wins + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

    if user.lower() == 'p' and machine == 1:
        print("User Won")
        wins = wins + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 'p' and machine == 3:
        print("User Lost")
        loss = loss + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

    if user.lower() == 's' and machine == 2:
        print("User Won")
        wins = wins + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 's' and machine == 1:
        print("User Lost")
        loss = loss + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)


