N = int(input())
board = [[0 for x in range(N)] for y in range(N)]
count = 0
column = [0 for i in range(N)]
Posdiag = [0 for i in range(2*N-1)]
Negdiag = [0 for i in range(2*N-1)]
def printSolution(board,N):
    for i in range(N):
        print(board[i])
    print()
    return
def search(queen):
    global count
    if(queen==N):
        printSolution(board,N)
        count += 1
        return
    for x in range(N):
        if(column[x] or Posdiag[x+queen] or Negdiag[x-queen+N-1]):
            continue
        board[x][queen] = 1
        column[x] = Posdiag[x+queen] = Negdiag[x-queen+N-1] = 1
        search(queen+1)
        board[x][queen] = 0
        column[x] = Posdiag[x+queen] = Negdiag[x-queen+N-1] = 0
search(0)
print(count)