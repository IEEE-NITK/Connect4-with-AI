#CLI version of Connect-4 Game

# import numpy as np

MAX_COLS = 7#maximum columns
MAX_ROWS = 6#maximum rows
ongoing = True #Tells if the game is ongoing
moves = 0 #number of moves till now

#creating a board for the new game   
def create_board():
	return [[0 for i in range(MAX_COLS)] for j in range(MAX_ROWS)]

#check if column is valid
def valid_choice(board, col):
	if(0<=col<=MAX_ROWS):
	    if(board[0][col] == 0):
		    return True
	return False

#put the piece on the board
def drop_piece(board, col, row, who_moved):
    board[row][col] = who_moved

#get the first free row
def get_row(board, col):
	for i in range(MAX_ROWS-1,-1,-1):
		if(board[i][col] == 0):
			return i

#check if the last move was winning   
def winning_check(board, last_row, last_col,last):		
	#Horizontal checks
	for i in range(MAX_COLS-3):
		for j in range(4):
			if(board[last_row][i+j] != last):
				break
			if(j == 3):
				return last

	#vertical checks
	for i in range(MAX_ROWS-3):
		for j in range(4):
			if(board[i+j][last_col] != last):
				break
			if(j == 3):
				return last

	#right diagonal checks (\)
	for i in range(MAX_ROWS-3):
		for j in range(MAX_COLS-3):
			for k in range(4):
				if(board[i+k][j+k] != last):
					break
				if(k == 3):
					return last

	#left diagonal checks (/)
	for i in range(3,MAX_ROWS,1):
		for j in range(MAX_COLS-3):
			for k in range(4):
				if(board[i-k][j+k] != last):
					break
				if(k == 3):
					return last
	return 0


#Creating the board
board = create_board()

def print_board(board):
    	for i in range(MAX_ROWS):
		    for j in range(MAX_COLS):
			    print(board[i][j],end=" ")
		    print("")
			
#Let the games begin!!				
while(ongoing):							 
	print_board(board)
	col = int(input("Enter a  column "))
	if moves%2==0:
    		l=1
	else:
    		l=2

	if(valid_choice(board,col)):
		row = get_row(board,col)
		drop_piece(board, col, row,l)
		win = winning_check(board, row, col,l)
		moves += 1
		if(win>0):
			print_board(board)
			print("Player",win,"has won")
			break
		if(moves == 42):
			print_board(board)
			print("Draw!")
			break
	else:
		print("Invalid column")



	#If number of moves is even Player 1 is going to move
		#If choice is valid
		#If choice isn't valid

	#If number of moves is odd Player 2 is going to move
		#If choice is valid
		#If choice isn't valid
    
        
