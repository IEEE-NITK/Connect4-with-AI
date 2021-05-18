n = int(input())
col = [0 for i in range(n)]
posdiag = [0 for i in range(2*n)]
negdiag = [0 for i in range(2*n)]
queens = 0
count = 0
positions = [0 for i in range(n)]
def printarr():
    for i in range(n):
        for j in range(n):
            if(positions[i] == j):
                print("Q",end=" ")
            else:
                print("X",end=" ")
        print("")
    print("")

def place(queens):
    global count
    global positions
    if(queens == n):
        count+=1
        printarr()
    else:
        for i in range(n):
            if(col[i] == 0 and posdiag[queens + i] == 0 and negdiag[n-1+queens-i] == 0):
                col[i] = 1
                posdiag[queens + i] = 1
                negdiag[n-1+queens-i] = 1
                positions[queens] = i
                place(queens + 1)
                col[i] = 0
                posdiag[queens + i] = 0
                negdiag[n-1+queens-i] = 0
                positions[queens] = 0
            else:
                continue
place(0)
print(count)