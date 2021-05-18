#CLI version of Connect-4 Game

# import numpy as np
import math
import random
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

def winning_check(board, piece):
		# Check horizontal locations for win
	for c in range(MAX_COLS-3):
		for r in range(MAX_ROWS):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(MAX_COLS):
		for r in range(MAX_ROWS-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(MAX_COLS-3):
		for r in range(MAX_ROWS-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(MAX_COLS-3):
		for r in range(3, MAX_ROWS):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def evaluate(w,piece):
    score = 0
    if piece == 2:
        opp_piece =1
    else:
        opp_piece = 2
    if w.count(piece) == 3 and w.count(0) == 1:
        score += 5
    elif w.count(piece) == 2 and w.count(0) == 2:
        score +=2
    if w.count(opp_piece) == 3 and w.count(0) == 1:
        score -= 40
    elif w.count(opp_piece) == 2 and w.count(0) == 2:
        score -= 10
    return score

def score(board,piece):
    score = 0
    col_arr = [[board[i][j] for i in range (MAX_ROWS)] for j in range (MAX_COLS)]
    center_arr = col_arr[MAX_COLS//2]
    score += center_arr.count(piece)*3

    #checking for rows
    for i in range (MAX_ROWS):
        for j in range (MAX_COLS-3):
            r = board[i][j:j+4]
            score += evaluate(r,piece)
    #checking for columns
    for i in range (MAX_COLS):
        for j in range (MAX_ROWS-3):
            c = col_arr[i][j:j+4]
            score += evaluate(c,piece)
    #positive diagonals
    for i in range (MAX_ROWS-1,2,-1):
        for j in range (MAX_COLS-3):
            pd = [board[i-x][j+x] for x in range (4)]
            score += evaluate(pd,piece)
    #negative diagonals
    for i in range (MAX_ROWS-1,2,-1):
        for j in range (MAX_COLS-1,2,-1):
            nd = [board[i-x][j-x] for x in range (4)]
            score += evaluate(nd,piece)
    
    return score

def get_valid_locations(board):
    valid_loc = []
    for col in range(MAX_COLS):
        if valid_choice(board,col):
            valid_loc.append(col)
    return valid_loc

def minimax(board,depth,maximizingplayer):
    if winning_check(board, 2):
        return(None, 100000000000000)
    if winning_check(board,1):
        return(None, -100000000000000)
    if moves > 42:
        return(None,0)
    if depth == 0:
        return(None, score(board,2))
    if maximizingplayer:
        value = -math.inf
        column = random.choice(get_valid_locations(board))
        for col in get_valid_locations(board):
            row = get_row(board,col)
            drop_piece(board,col,row,2)
            new_score = minimax(board, depth-1, False)[1]
            drop_piece(board,col,row,0)
            if new_score>value:
                value = new_score
                column = col
        return column,value
    
    else:
        value = math.inf
        column = random.choice(get_valid_locations(board))
        for col in get_valid_locations(board):
            row = get_row(board,col)
            drop_piece(board,col,row,1)
            new_score = minimax(board,depth-1,True)[1]
            drop_piece(board,col,row,0)
            if new_score < value:
                value = new_score
                column = col
        return column,value


def print_board(board):
	for i in range(MAX_ROWS):
		for j in range(MAX_COLS):
			print(board[i][j],end=" ")
		print(" ")
	print("")

    


board = create_board()
print("Enter 1 to play against computer, 2 to play 2 player game")
mode = int(input())	
if (mode == 2):			
	while(ongoing):							 
		print_board(board)
		col = int(input("Enter the column number "))
		if moves%2==0:
			l=1
		else:
			l=2

		if(valid_choice(board,col)):
			row = get_row(board,col)
			drop_piece(board, col, row,l)
			win = winning_check(board,l)
			moves += 1
			if(win):
				print_board(board)
				print("Player",l,"has won")
				break
			if(moves == 42):
				print_board(board)
				print("Draw!")
				break
		else:
			print("Invalid column")

if (mode == 1):
    print("Enter the depth value")
    depth = int(input())
    while ongoing:
        if moves%2 == 0:
            l = 1
        else:
            l = 2
        print_board(board)
        if l == 1:
            col = int(input("Enter the column number "))
            vc = valid_choice(board,col)
            if (vc == False):
                print("Invalid column")
                col = int(input("Enter the column number "))
        else:
            col, minimax_score = minimax(board,depth, True)
        row = get_row(board,col)
        drop_piece(board,col,row,l)
        win = winning_check(board, l)
        moves += 1
        if (win):
            print_board(board)
            print("Player", l, "wins!")
            break
        if moves >= 42:
            print_board(board)
            print("DRAW!")
            break
    


        
