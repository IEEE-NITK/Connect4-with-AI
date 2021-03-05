n,m,k,w = map(int, input().split()) 
matrix = []
for i in range (n):
    s1 = input().split()
    matrix.append([])
    for j in range (m):
        matrix[i].append(int(s1[j]))
x = -1
for i in range (n):
    for j in range (m-w+1):
        a = matrix[i][j]
        for l in range (j+1,j+w):
            if matrix[i][l] != a:
                x = -1
                break
            else:
                x = a
        if(x>-1):
            break
    if(x>-1):
        break
if(x == -1):
    for i in range (n-w+1):
        for j in range (m):
            a = matrix[i][j]
            for l in range (i+1,i+w):
                if matrix[l][j] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                break
        if(x>-1):
            break
if(x == -1):
    for i in range (n-1,w-2,-1):
        for j in range (m-w+1):
            a = matrix[i][j]
            for l in range(1,w):
                if matrix[i-l][j+l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                break
        if(x>-1):
            break         
if(x == -1):
    for i in range (n-1,w-2,-1):
        for j in range (m-1,w-2,-1):
            a = matrix[i][j]
            for l in range(1,w):
                if matrix[i-l][j-l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                break
        if(x>-1):
            break         

print(x)

