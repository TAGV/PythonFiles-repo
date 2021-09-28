#Tic Tac Toe board game

import time
import random



tboard = {'1':1,'2':2,'3':3,
          '4':4,'5':5,'6':6,
          '7':7,'8':8,'9':9}

player1 = None
player2 = None

def checkGameWinner(board):
    for items in board.values():
        if (board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X')\
                or (board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X')\
                or (board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X')\
                or (board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X')\
                or (board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X')\
                or (board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X')\
                or (board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X')\
                or (board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X'):
            return True
        elif (board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O') \
                or (board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O') \
                or (board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O') \
                or (board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O') \
                or (board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O') \
                or (board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O') \
                or (board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O') \
                or (board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O'):
            return True
        else:
            return False



def welcomeMessg():
    print("-------Welcome to the Tic-Tac-Toe-------")

def players():
    global player1,player2
    player1 = input("Enter your name Player1:\t")
    player2 = input("Enter your name Player2:\t")

def toss():
    global player1, player2
    chance = random.randint(0,1)
    if chance == 0:
        return player1
    else:
        return player2

def printboard(board):
    print("\t\t\t\t",str(board['1']) + '|' + str(board['2']) + '|' + str(board['3']))
    print("\t\t\t\t","-+-+-")
    print("\t\t\t\t",str(board['4']) + '|' + str(board['5']) + '|' + str(board['6']))
    print("\t\t\t\t","-+-+-")
    print("\t\t\t\t",str(board['7']) + '|' + str(board['8']) + '|' + str(board['9']))


welcomeMessg()
printboard(tboard)
players()
print("Waiting for Toss..........")
time.sleep(1)

# Playing the Game

counter = 0
secondplayer = None

firstplayer = toss()
if firstplayer == player1:
    secondplayer = player2
elif firstplayer == player2:
    secondplayer = player1

#for i in range(9):
move1 = None
while True:
    turn = 'X'
    move = (input("Enter your position(1,2,3,4,5,6,7,8,9)..."+firstplayer+"\t"))
    if move == move1:
        print("Already filled. Enter another position ")
        continue
    if tboard.get(move,0) == 0:
        print(move)
        continue
    tboard[move] = turn
    if checkGameWinner(tboard) == True:
        print(firstplayer + " is the winner")
        break
    printboard(tboard)
    counter += 1
    if counter == 9:
        break
    if turn == 'X':
        while True:
            move1 = (input("Enter your position(1,2,3,4,5,6,7,8,9)..."+secondplayer+"\t"))
            if move1 == move:
                print("Already filled. Enter another position ")
                continue
            turn = 'O'
            if tboard.get(move1,0) == 0:
                print("Wrong Input ")
                continue
            tboard[move1] = turn
            printboard(tboard)
            break
        if checkGameWinner(tboard) == True:
            print(secondplayer + " is the winner")
            break
        counter += 1
        if counter == 9:
            break

if checkGameWinner(tboard) == False:
    print("Its a Tie. Try Again!!!!")
print()
print("\t\t=======Game Over=======")
printboard(tboard)
