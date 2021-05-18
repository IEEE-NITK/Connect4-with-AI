def consec():
    min_div = w-1
    max_div1 = n-w+1
    max_div2 = m-w+1
    #horizontal
    for i in range(n):
        for j in range(max_div2):
            temp = grid[i][j]
            for l in range(w):
                if(grid[i][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
    #vertical
    for i in range(max_div1):
        for j in range(m):
            temp = grid[i][j]
            for l in range(w):
                if(grid[i+l][j] != temp):
                    break
                elif(l == min_div):
                    return temp
    #negative diag
    for i in range(max_div1):
        for j in range(max_div2):
            temp = grid[i][j]
            for l in range(w):
                if(grid[i+l][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
    #positive diag
    for i in range(min_div,n,1):
        for j in range(max_div2):
            temp = grid[i][j]
            for l in range(w):
                if(grid[i-l][j+l] != temp):
                    break
                elif(l == min_div):
                    return temp
    return -1



n,m,k,w = list(map(int,input().split()))
grid = []
for i in range(n):
    grid.append(list(map(int,input().split())))
print(consec())