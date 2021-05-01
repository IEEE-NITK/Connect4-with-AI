#CLI version of Connect-4 Game

# import numpy as np

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
def winning_check(board, last_row, last_col,last):
    x = -1
    a = last
    #checking only the last row
    for j in range (MAX_COLS-3):
        for l in range (j,j+4):
            if board[last_row][l] != a:
                x = -1
                break
            else:
                x = a
        if(x>-1):
            return x
    #checking only the last column
    for i in range (MAX_ROWS-3):
        for l in range (i,i+4):
            if board[l][last_col] != a:
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

#Let the games begin!!				
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
    w = winning_check(board,r,c,p)
    if(w>0):
        for i in range (MAX_ROWS):
            print(*board[i])
        print("GAME OVER!")
        print("PLAYER",p,"HAS WON!", sep = ' ')
        ongoing = False
    if(moves >= 42):
        print("GAME OVER!")
        for i in range (MAX_ROWS):
            print(*board[i])
        print("DRAW")
        ongoing = False

	#If number of moves is even Player 1 is going to move
		#If choice is valid
		#If choice isn't valid

	#If number of moves is odd Player 2 is going to move
		#If choice is valid
		#If choice isn't valid