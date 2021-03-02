#The grid in question is divided into 5 sections
#each cell in every section except 5 is travelled once and is used as anchor point
###############################################
#    sec 1                    #               #
#    neg diag, hor, ver       #    sec 2      #
#                             #     ver       #
###############################               #
#    sec 3                    #               #
#    neg diag, pos diag,      #               #
#    hor,ver                  #               #
###############################################
#    sec 4                    #    sec 5      #
#    pos diag, hor            #    nothing    #
###############################################
def consec(grid,n,m,w):
    match = False
    min_div = w-1
    max_div = n-w+1 #these two are declared here since computing them each time could take time
    #sec 1
    for i in range(min_div):#min_div = w-1
        for j in range(max_div):#max_div = n-w+1
            temp = grid[i][j]
            for l in range(w):#horizontal
                if(grid[i][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
            for l in range(w):#vertical
                if(grid[i+l][j] != temp):
                    break
                elif(l == min_div):
                    return temp
            for l in range(w):#neg slope diag
                if(grid[i+l][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
    #sec 2
    for i in range(max_div):
        for j in range(max_div,n,1):
            for l in range(w):#vertical
                temp = grid[i][j]
                if(grid[i+l][j] != temp):
                    break
                elif(l == min_div):
                    return temp
    #sec 3
    for i in range(min_div,max_div,1):
        for j in range(max_div):
            temp = grid[i][j]
            for l in range(w):#horizontal
                if(grid[i][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
            for l in range(w):#vertical
                if(grid[i+l][j] != temp):
                    break
                elif(l == min_div):
                    return temp
            for l in range(w):#neg slope diag
                if(grid[i+l][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
            for l in range(w):#pos diag
                if(grid[i-l][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
    #sec 4
    for i in range(max_div,n):
        for j in range(max_div):
            temp = grid[i][j]
            for l in range(w):#horizontal
                if(grid[i][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
            for l in range(w):#pos diag
                if(grid[i-l][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
    #if nothing is ever returned
    return -1

n,m,k,w = list(map(int,input().split()))
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
print(consec(board,n,m,w))