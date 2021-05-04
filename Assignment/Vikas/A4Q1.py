MAX_COLS = 7#maximum columns
MAX_ROWS = 6#maximum rows
ONGOING = True #Tells if the game is ongoing
MOVES = 0 #number of moves till now
INFP = 1000000
INFN = -1000000

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

#def score(count):
	#if(temp == 1):
		#sign = 1
	#else:
		#sign = -1
	#u = (100**count)*sign#10000 for 3 in a row, 100 for 2 in a row, 1 for 1 in a row(this makes sense since an open piece is more valuable than closed piece)
	#sreturn u

def eval(board):#This function is better if winning check is called before it
	utility = 0 #utility is calculated considering first player as maximizer and second player as minimizer
	#horizontal 
	for i in range(MAX_ROWS):
		for j in range(MAX_COLS):
			if(board[i][j] != 0):
				continue
			countarr = [0,0]#Keeps track of maximum in a row ending at current position for each colour/player
			#left
			if(j>1):
				temp = board[i][j-1]
				if(temp != 0):
				    count = 1
				    for k in range(j-2,-1,-1):
					    if(board[i][k] != temp):
						    break
					    count += 1					
				    countarr[temp - 1] = max(countarr[temp - 1],count)
			#right
			if(j<MAX_COLS-2):
				temp = board[i][j+1]
				if(temp != 0):
				    count = 1
				    for k in range(j+2,MAX_COLS,1):
					    if(board[i][k] != temp):
						    break
					    count += 1
				    countarr[temp - 1] = max(countarr[temp - 1],count)
			#down(there is no up since an empty space cannot have pieces directly above)
			if(i<MAX_ROWS-2):
				temp = board[i+1][j]
				if(temp != 0):
				    count = 1
				    for k in range(i+2,MAX_ROWS,1):
					    if(board[k][j] != temp):
						    break
					    count += 1
				    countarr[temp - 1] = max(countarr[temp - 1],count)
			#negitive diagonal downwards
			if(i<MAX_ROWS-2 and j<MAX_COLS-2):
				temp = board[i+1][j+1]
				if(temp != 0):
					count = 1
					limit = min(MAX_COLS - j,MAX_ROWS - i)
					for k in range(2,limit,1):
						if(board[i+k][j+k] != temp):
							break
						count += 1
					countarr[temp - 1] = max(countarr[temp - 1],count)
			#negative diagonal upwards
			if(i>1 and j>1):
				temp = board[i-1][j-1]
				if(temp!=0):
					count = 1
					limit = min(i+1,j+1)
					for k in range(2,limit,1):
						if(board[i-k][j-k] != temp):
							break
						count += 1
					countarr[temp - 1] = max(countarr[temp - 1],count)
			#positive diagonal upwards
			if(i>1 and j<MAX_COLS - 2):
				temp = board[i-1][j+1]
				if(temp != 0):
					count = 1
					limit = min(i+1,MAX_COLS-j)
					for k in range(2,limit,1):
						if(board[i-k][j+k] != temp):
							break
						count+= 1
					countarr[temp - 1] = max(countarr[temp - 1],count)
			#positive diagonal downwards
			if(i<MAX_ROWS-2 and j>1):
				temp = board[i+1][j-1]
				if(temp != 0):
					count = 1
					limit = min(j+1,MAX_ROWS-i)
					for k in range(2,limit,1):
						if(board[i+k][j-k] != temp):
							break
						count += 1
					countarr[temp - 1] = max(countarr[temp - 1],count)
			
			if(countarr[0] > 0):
				utility += 100**(countarr[0]-1)#10000 for 3 in a row, 100 for 2 in a row, 1 for 1 in a row(this makes sense since an open piece is more valuable than closed piece)
			if(countarr[1] > 0):
				utility -= 100**(countarr[1]-1)
	return utility

def minimax(arr,depth,isMax,moves, last_row, last_col):
	winner = winning_check(arr, last_row, last_col)
	if(winner == 1):
		return INFP
	if(winner == 2):
		return INFN
	if(moves == 42):
		return 0
	if(depth == 0):
		return eval(arr)
	if(isMax):
		value = INFN
		for j in range(MAX_COLS):
			if(valid_choice(arr,j)):
				i = get_row(arr,j)
				arr[i][j] = 1
				value = max(value,minimax(arr,depth-1,False,moves+1,i,j))
				arr[i][j] = 0
		return value
	else:
		value = INFP
		for j in range(MAX_COLS):
			if(valid_choice(arr,j)):
				i = get_row(arr,j)
				arr[i][j] = 2
				value = min(value,minimax(arr,depth-1,True,moves+1,i,j))
				arr[i][j] = 0
		return value






def print_board(board):
	for i in range(MAX_ROWS):
		for j in range(MAX_COLS):
			print(board[i][j],end=" ")
		print("")

board = create_board()
print("Enter 1 to play against computer, 2 to play 2 player mode")
mode = int(input())
if(mode == 2):
	while(True):							 
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
			    print("Player",winner,"has won the game in",MOVES,"moves!!!")
			    break
		    if(MOVES == 42):
			    print_board(board)
			    print("Draw!")
			    break
	    else:
		    print("You entered an invalid column number")
elif(mode == 1):
	print("Enter the depth of the computer engine")
	dep = int(input())
	print("Enter 1 to go first and 2 to go second")
	first = int(input())
	if(first == 1):
		while(True):
			print_board(board)
			print("Enter a valid column number")
			col = int(input())
			if(valid_choice(board,col)):
				row = get_row(board,col)
				board[row][col] = 1
				winner = winning_check(board,row,col)
				MOVES += 1
				if(winner):
					print_board(board)
					print("Player has won the game in",MOVES,"moves!!!")
					break
				if(MOVES == 42):
					print_board(board)
					print("Draw!")
					break
				best = INFP
				bestMove = [0,0]
				for j in range(MAX_COLS):
					if(valid_choice(board,j)):
						i = get_row(board,j)
						board[i][j] = 2
						value = minimax(board, dep,True,MOVES+1,i,j)
						if(value <= best):
							bestMove = [i,j]
							best = value
						board[i][j] = 0
				board[bestMove[0]][bestMove[1]] = 2
				winner = winning_check(board,bestMove[0],bestMove[1])
				MOVES += 1
				if(winner):
					print_board(board)
					print("Computer has won the game in",MOVES,"moves!!!")
					break
				if(MOVES == 42):
					print_board(board)
					print("Draw!")
					break

			else:
				print("You entered an invalid column number")
	else:
		board[MAX_ROWS-1][3] = 1#This is the optimal move i googled (Serious reason because player going first then computer responding is easier to handle than computer going first, because the player may make invalid moves)
		MOVES += 1
		while(True):
			print_board(board)
			print("Enter a valid column number")
			col = int(input())
			if(valid_choice(board,col)):
				row = get_row(board,col)
				board[row][col] = 2
				winner = winning_check(board,row,col)
				MOVES += 1
				if(winner):
					print_board(board)
					print("Player has won the game in",MOVES,"moves!!!")
					break
				if(MOVES == 42):
					print_board(board)
					print("Draw!")
					break
				best = INFN
				bestMove = [0,0]
				for j in range(MAX_COLS):
					if(valid_choice(board,j)):
						i = get_row(board,j)
						board[i][j] = 1
						value = minimax(board, dep,False,MOVES+1,i,j)
						if(value >= best):
							bestMove = [i,j]
							best = value
						board[i][j] = 0
				board[bestMove[0]][bestMove[1]] = 1
				winner = winning_check(board,bestMove[0],bestMove[1])
				MOVES += 1
				if(winner):
					print_board(board)
					print("Computer has won the game in",MOVES,"moves!!!")
					break
				if(MOVES == 42):
					print_board(board)
					print("Draw!")
					break

			else:
				print("You entered an invalid column number")