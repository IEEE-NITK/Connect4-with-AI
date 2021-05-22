n = int(input())
def create_board():
    return[[0 for j in range (n)] for i in range (n)]
def printboard(b,n):
    for i in range (n):
        print(*b[i])
    print()
    return
board = create_board()
c = 0
col = []
diag1 = []
diag2 = []
for i in range (n):
    col.append(0)
for i in range (2*n-1):
    diag1.append(0)
    diag2.append(0)
def search(y):
    if(y==n):
        printboard(board,n)
        global c
        c += 1
        return
    for x in range(n):
        if(col[x] or diag1[x+y] or diag2[x-y+n-1]):
            continue
        board[x][y] = 1
        col[x] = diag1[x+y] = diag2[x-y+n-1] = 1
        search(y+1)
        board[x][y] = 0
        col[x] = diag1[x+y] = diag2[x-y+n-1] = 0
search(0)
print(c)