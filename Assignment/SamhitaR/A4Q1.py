#CLI version of Connect-4 Game

# import numpy as np

from math import inf
import random

MAX_COLS = 7#maximum rows
MAX_ROWS = 6#maximum columns
ongoing = True #Tells if the game is ongoing
moves = 0 #number of moves till now

#creating a board for the new game   
def create_board():
	return[[0 for j in range (MAX_COLS)] for i in range (MAX_ROWS)]

#check if column is valid
def valid_choice(board, col):
    if(0<=col<MAX_COLS) and board[0][col] == 0:
        return True
    return False

#put the piece on the board
def drop_piece(board, col, row, who_moved):
	board[row][col] = who_moved

#get the first free row
def get_row(board, col):
	for i in range (MAX_ROWS-1,-1,-1):
         if board[i][col] == 0:
            return i 

#check if the last move was winning   
def winning_check(board,player):
    x = -1
    a = player
    #checking rows
    for i in range (MAX_ROWS):
        for j in range (MAX_COLS-3):
            for l in range (j,j+4):
                if board[i][l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x
    #checking columns
    for i in range (MAX_ROWS-3):
        for j in range (MAX_COLS):
            for l in range (i,i+4):
                if board[l][j] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x
    #checking positive diagonals
    for i in range (MAX_ROWS-1,2,-1): 
        for j in range (MAX_COLS-3):
            for l in range(0,4):
                if board[i-l][j+l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x   
    #checking negative diagonals
    for i in range (MAX_ROWS-1,2,-1):
        for j in range (MAX_COLS-1,2,-1):
            for l in range(0,4):
                if board[i-l][j-l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x
    return x

#Creating the board
board = create_board()
#evaluating scores
def evaluate(a,p):
    s = 0
    if p == 2:
        opp = 1
    else:
        opp = 2
    #if a.count(p) == 4:
    #    s += 10000
    if a.count(p) == 3 and a.count(0) == 1:
        s += 10
    elif a.count(p) == 2 and a.count(0) == 2:
        s += 7
    #deducting scores if the opponent has an advantage
    #if a.count(opp) == 4:
    #    s -= 10000
    if a.count(opp) == 3 and a.count(0) == 1:
        s -= 70
    elif a.count(opp) == 2 and a.count(0) == 2:
        s -= 15
    return s
#assigning scores for moves
def score(board,p):
    s = 0
    #checking for rows
    for i in range (MAX_ROWS):
        for j in range (MAX_COLS-3):
            r = board[i][j:j+4]
            s += evaluate(r,p)
    #checking for columns
    col_arr = [[board[i][j] for i in range (MAX_ROWS)] for j in range (MAX_COLS)]
    for i in range (MAX_COLS):
        for j in range (MAX_ROWS-3):
            c = col_arr[i][j:j+4]
            s += evaluate(c,p)
    #positive diagonals
    for i in range (MAX_ROWS-1,2,-1):
        for j in range (MAX_COLS-3):
            pd = [board[i-x][j+x] for x in range (4)]
            s += evaluate(pd,p)
    #negative diagonals
    for i in range (MAX_ROWS-1,2,-1):
        for j in range (MAX_COLS-1,2,-1):
            nd = [board[i-x][j-x] for x in range (4)]
            s += evaluate(nd,p)
    #giving preference for center col so its easier to build stuff in the future
    center_arr = col_arr[MAX_COLS//2]
    s += center_arr.count(p)*7
    return s
def valid_cols(board):
    v = []
    for i in range(MAX_COLS):
        if(valid_choice(board,i)):
            v.append(i)
    return v
def minimax(board,max_player,d):
    if winning_check(board,2)>0:
        return (None,inf)
    if winning_check(board,1)>0:
        return (None,-inf)
    if moves > 42:
        return (None,0)
    if d == 0:
        return (None,score(board,2))
    if max_player:
        val = -inf
        col = random.choice(valid_cols(board))
        for c in valid_cols(board):
            r = get_row(board,c)
            drop_piece(board,c,r,2)
            s = minimax(board,False,d-1)[1]
            drop_piece(board,c,r,0)
            if s> val:
                val = s
                col = c
        return col,val
    else:
        val = inf
        col = random.choice(valid_cols(board))
        for c in valid_cols(board):
            r = get_row(board,c)
            drop_piece(board,c,r,1)
            s = minimax(board,True,d-1)[1]
            drop_piece(board,c,r,0)
            if s< val:
                val = s
                col = c
        return col,val

#Let the games begin!!
print("To play against the computer enter 1:")
print("To have a 2 player game enter 2:")
mode = int(input())				
if mode == 1:
    while ongoing:
        if(moves%2 == 0):
            p = 1
        else:
            p = 2
        for i in range (MAX_ROWS):
            print(*board[i])
        print()
        if p == 1:
            c = int(input("Enter the column:"))
            b = valid_choice(board,c)
            while (b == False):
                c = int(input("Enter the column:"))
                b = valid_choice(board,c)
        else:
            c, minimax_score = minimax(board,True,2)
            #print(minimax_score)
        r = get_row(board,c)
        drop_piece(board,c,r,p)
        moves += 1
        w = winning_check(board,p)
        if(w>0):
            for i in range (MAX_ROWS):
                print(*board[i])
            print("GAME OVER!")
            print("PLAYER",p,"HAS WON!", sep = ' ')
            ongoing = False
            break
        if(moves >= 42):
            print("GAME OVER!")
            for i in range (MAX_ROWS):
                print(*board[i])
            print("DRAW")
            ongoing = False
if mode == 2:
    while ongoing:							 
        for i in range (MAX_ROWS):
             print(*board[i])
        if (moves%2 == 0):
            p = 1
        else:
            p = 2
        c = int(input("Enter the column:"))
        b = valid_choice(board,c)
        while (b == False):
            c = int(input("Enter the column:"))
            b = valid_choice(board,c)
        r = get_row(board,c)
        drop_piece(board,c,r,p)
        moves += 1
        w = winning_check(board,p)
        if(w>0):
            for i in range (MAX_ROWS):
                print(*board[i])
            print("GAME OVER!")
            print("PLAYER",p,"HAS WON!", sep = ' ')
            ongoing = False
            break
        if(moves >= 42):
            print("GAME OVER!")
            for i in range (MAX_ROWS):
                print(*board[i])
            print("DRAW")
            ongoing = False
