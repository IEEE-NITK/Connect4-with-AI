#CLI version of Connect-4 Game

# import numpy as np

MAX_COLS = 7#maximum columns
MAX_ROWS = 6#maximum rows
ONGOING = True #Tells if the game is ongoing
MOVES = 0 #number of moves till now

#creating a board for the new game   
def create_board():
	return [[0 for i in range(MAX_COLS)] for j in range(MAX_ROWS)]
	
	

#check if column is valid
def valid_choice(board, col):
	if(col>=0 and col<= 6):
	    if(board[0][col] == 0):
		    return True
	return False

#put the piece on the board

#get the first free row
def get_row(board, col):
	for i in range(MAX_ROWS-1,-1,-1):
		if(board[i][col] == 0):
			return i
#check if the last move was winning   
def winning_check(board, last_row, last_col):		
	#Horizontal checks
	for i in range(MAX_COLS-3):#Beyond MAX_COLS-3 insufficient pieces for 4 in a row
		temp = board[last_row][i]
		for j in range(4):
			if(board[last_row][i+j] != temp or temp == 0):
				break
			if(j == 3):
				return temp
		
	#vertical checks
	for i in range(MAX_ROWS-3):#Beyond MAX_ROWS-3 insufficient pieces for 4 in a row
		temp = board[i][last_col]
		for j in range(4):
			if(board[i+j][last_col] != temp or temp == 0):
				break
			if(j == 3):
				return temp
				
	#right diagonal checks (\)
	for i in range(MAX_ROWS-3):
		for j in range(MAX_COLS-3):
			temp = board[i][j]
			for k in range(4):
				if(board[i+k][j+k] != temp or temp == 0):
					break
				if(k == 3):
					return temp

	#left diagonal checks (/)
	for i in range(3,MAX_ROWS,1):
		for j in range(MAX_COLS-3):
			temp = board[i][j]
			for k in range(4):
				if(board[i-k][j+k] != temp or temp == 0):
					break
				if(k == 3):
					return temp
	return 0

def print_board(board):
	for i in range(MAX_ROWS):
		for j in range(MAX_COLS):
			print(board[i][j],end=" ")
		print("")
	
#Creating the board
board = create_board()
#Let the games begin!!				
while(ONGOING):							 
	print_board(board)
	print("Enter a valid column number")
	col = int(input())
	if(valid_choice(board,col)):
		row = get_row(board,col)
		board[row][col] = (MOVES%2) + 1
		winner = winning_check(board, row, col)
		MOVES += 1
		if(winner):
			print_board(board)
			print("Player",winner,"has won the game in",MOVES,"moves")
			break
		if(MOVES == 42):#answer to the ultimate question
			print_board(board)
			print("Draw!")
			break
	else:
		print("You entered an invalid column number")


	
	#If number of moves is even Player 1 is going to move
		#If choice is valid
		#If choice isn't valid

	#If number of moves is odd Player 2 is going to move
		#If choice is valid
		#If choice isn't valid
