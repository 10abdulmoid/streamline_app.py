#importing modules
import os
import time

#empty positions initialzed
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

Win = 1;Draw = -1
Running = 0;Stop = 1

Game = Running
point = 'X'

#printing board to console
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")


def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False
#test win or lose condition
def CheckWin():
    global Game

 #check win in rows
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
   #in columns 
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
#in diagnols    
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
#cheching drawe condition
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
    else:
        Game = Running


print("tic tac toe by Abdul Moid")
print("Player 1 [X] 1Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)

#clearing screen
while Game == Running:
    os.system('cls')
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        point = 'X'
    else:
        print("Player 2's chance")
        point = 'O'

    choice = int(input("Enter the position between [1-9] where you want to point: "))
    if CheckPosition(choice):
        board[choice] = point
        player += 1
        CheckWin()

    os.system('cls')
    DrawBoard()

    if Game == Draw:
        print("Game Draw-try again")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("player 1 wins!")
        else:
            print("Player 2 Wins!")