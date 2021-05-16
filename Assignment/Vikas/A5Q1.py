import pygame

pygame.init()

BLACK = (0,0,0)
RED = (235,0,0)
YELLOW = (255,255,0)
GREY = (220,220,220)
WHITE = (255,255,255)
DARK_VIOLET = (81, 18, 129)
LIME_GREEN = (165, 225, 173)

WINNER_FONT = pygame.font.SysFont('arial', 75)
FINISH_FONT = pygame.font.SysFont('arial', 100)

MAX_COLS = 7#maximum columns
MAX_ROWS = 6#maximum rows
ONGOING = True #Tells if the game is ongoing
MOVES = 0 #number of moves till now
INFP = 100000000
INFN = -100000000

WIDTH = (MAX_COLS)*100
HEIGHT = (MAX_ROWS + 1)*100
SIZE = (WIDTH,HEIGHT)

screen = pygame.display.set_mode(SIZE)
screen.fill(DARK_VIOLET)

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

def minimax(arr,depth,alpha,beta,isMax,moves, last_row, last_col):
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
				value = max(value,minimax(arr,depth-1,alpha,beta,False,moves+1,i,j))
				alpha = max(value,alpha)
				arr[i][j] = 0
				if(alpha >= beta):
					break
		return value
	else:
		value = INFP
		for j in range(MAX_COLS):
			if(valid_choice(arr,j)):
				i = get_row(arr,j)
				arr[i][j] = 2
				value = min(value,minimax(arr,depth-1,alpha,beta,True,moves+1,i,j))
				beta = min(value,beta)
				arr[i][j] = 0
				if(beta <= alpha):
					break
		return value

def draw_board():
	pygame.draw.rect(screen,LIME_GREEN,(0,0,WIDTH,100))
	for r in range(MAX_ROWS + 1):
		for c in range(MAX_COLS):
			pygame.draw.circle(screen,GREY,(c*100 + 50,r*100 + 50),40)
	pygame.display.update()

def change_board(board,c,r,moves):
	if(moves&1):
		pygame.draw.circle(screen, YELLOW, (c*100 + 50, r*100 + 150), 40)
		pygame.draw.circle(screen, RED, (c*100 + 50, 50), 40)
	else:
		pygame.draw.circle(screen, RED, (c*100 + 50, r*100 + 150), 40)
		pygame.draw.circle(screen, YELLOW, (c*100 + 50, 50), 40)
	pygame.display.update()

def print_board(board):
	for i in range(MAX_ROWS):
		for j in range(MAX_COLS):
			print(board[i][j],end=" ")
		print("")

draw_board()
board = create_board()
#print("Enter 1 to play against computer, 2 to play 2 player mode")
#mode = int(input())
mode = 1
if(mode == 2):	
	while(ONGOING):						 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				ONGOING = False
				exit()

			if event.type == pygame.MOUSEMOTION:
				x_pos = event.pos[0]
				x_pos = (x_pos//100)*100 + 50
				for c in range(MAX_COLS):
					pygame.draw.circle(screen,GREY, (c*100 + 50,50),40)
				if(MOVES&1):
					pygame.draw.circle(screen,YELLOW, (x_pos,50),40)
				else:
					pygame.draw.circle(screen,RED,(x_pos,50),40)
				pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				x_val = event.pos[0]
				choice = x_val//100
				if(valid_choice(board,choice)):
					row = get_row(board, choice)
					board[row][choice] = (MOVES%2) + 1
					change_board(board,choice,row,MOVES)
					MOVES += 1
					winner = winning_check(board, row, choice)
					if(winner == 1):
						screen.blit(WINNER_FONT.render("Player 1 Won!", True, RED),(70,140))
						game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
						screen.blit(game_over, (60,240))
						ONGOING = False
						pygame.display.update()
						pygame.time.wait(8000)
					elif(winner == 2):
						screen.blit(WINNER_FONT.render("Player 2 Won!", True, YELLOW),(70,140))
						game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
						screen.blit(game_over, (60,240))
						ONGOING = False
						pygame.display.update()
						pygame.time.wait(8000)
					elif(MOVES == 42):
						screen.blit(WINNER_FONT.render("DRAW!", True, (0,255,0)),(70,140))
						game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
						screen.blit(game_over, (60,240))
						ONGOING = False
						pygame.display.update()
						pygame.time.wait(8000)


elif(mode == 1):
	#print("Enter the depth of the computer engine")
	#dep = int(input())
	dep = 4
	#print("Enter 1 to go first and 2 to go second")
	#first = int(input())
	first = 1
	if(first == 1):
		while(ONGOING):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ONGOING = False
					exit()

				if event.type == pygame.MOUSEMOTION:
					x_pos = event.pos[0]
					x_pos = (x_pos//100)*100 + 50
					for c in range(MAX_COLS):
						pygame.draw.circle(screen,GREY, (c*100 + 50,50),40)
					pygame.draw.circle(screen,RED,(x_pos,50),40)
					pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					x_val = event.pos[0]
					choice = x_val//100
					if(valid_choice(board, choice)):
						row = get_row(board,choice)
						board[row][choice] = 1
						change_board(board, choice, row, MOVES)
						MOVES += 1
						if(winning_check(board,row,choice)):
							screen.blit(WINNER_FONT.render("Player Won!", True, RED),(70,140))
							game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
							screen.blit(game_over, (60,240))
							ONGOING = False
							pygame.display.update()
							pygame.time.wait(8000)
						best = INFP
						bestMove = [0,0]
						for j in range(MAX_COLS):
							if(valid_choice(board,j)):
								i = get_row(board,j)
								board[i][j] = 2
								value = minimax(board, dep,INFN,INFP,True,MOVES+1,i,j)
								if(value == INFN):
									bestMove = [i,j]
									break
								if(value <= best):
									bestMove = [i,j]
									best = value
								board[i][j] = 0
						board[bestMove[0]][bestMove[1]] = 2
						change_board(board, bestMove[1], bestMove[0], MOVES)
						MOVES += 1
						if(winning_check(board,bestMove[0], bestMove[1])):
							screen.blit(WINNER_FONT.render("Computer Won!", True, YELLOW),(70,140))
							game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
							screen.blit(game_over, (60,240))
							ONGOING = False
							pygame.display.update()
							pygame.time.wait(8000)
						elif(MOVES == 42):
							screen.blit(WINNER_FONT.render("DRAW!", True, (0,255,0)),(70,140))
							game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
							screen.blit(game_over, (60,240))
							ONGOING = False
							pygame.display.update()
							pygame.time.wait(8000)
						

	else:
		board[MAX_ROWS-1][3] = 1#This is the optimal move i googled (Serious reason because player going first then computer responding is easier to handle than computer going first, because the player may make invalid moves)
		change_board(board, 3, MAX_ROWS - 1, MOVES)
		MOVES += 1
		while(ONGOING):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ONGOING = False
					exit()

				if event.type == pygame.MOUSEMOTION:
					x_pos = event.pos[0]
					x_pos = (x_pos//100)*100 + 50
					for c in range(MAX_COLS):
						pygame.draw.circle(screen,GREY, (c*100 + 50,50),40)
					pygame.draw.circle(screen,YELLOW,(x_pos,50),40)
					pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					x_val = event.pos[0]
					choice = x_val//100
					if(valid_choice(board, choice)):
						row = get_row(board,choice)
						board[row][choice] = 2
						change_board(board, choice, row, MOVES)
						MOVES += 1
						if(winning_check(board,row,choice)):
							screen.blit(WINNER_FONT.render("Player Won!", True, YELLOW),(70,140))
							game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
							screen.blit(game_over, (60,240))
							ONGOING = False
							pygame.display.update()
							pygame.time.wait(8000)
							break
						elif(MOVES == 42):
							screen.blit(WINNER_FONT.render("DRAW!", True, (0,255,0)),(70,140))
							game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
							screen.blit(game_over, (60,240))
							ONGOING = False
							pygame.display.update()
							pygame.time.wait(8000)
							break
						best = INFN
						bestMove = [0,0]
						for j in range(MAX_COLS):
							if(valid_choice(board,j)):
								i = get_row(board,j)
								board[i][j] = 1
								value = minimax(board, dep,INFN,INFP,False,MOVES+1,i,j)
								if(value == INFP):
									bestMove = [i,j]
									break
								if(value >= best):
									bestMove = [i,j]
									best = value
								board[i][j] = 0
						board[bestMove[0]][bestMove[1]] = 1
						print(best)
						change_board(board, bestMove[1], bestMove[0], MOVES)
						MOVES += 1
						if(winning_check(board,bestMove[0], bestMove[1])):
							screen.blit(WINNER_FONT.render("Computer Won!", True,RED),(70,140))
							game_over = FINISH_FONT.render("GAME OVER!", True, (0,255,0))
							screen.blit(game_over, (60,240))
							ONGOING = False
							pygame.display.update()
							pygame.time.wait(8000)
