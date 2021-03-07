l=list(map(int,input().split()))
n,m,k,w=l[0],l[1],l[2],l[3]
mat = []
s=-2
for i in range(n):
    b=list(map(int,input().split()))
    mat.append(b)

# Diagonal
for i in range(w-1,n,1):
    for j in range(m-w+1):
        p = mat[i][j]
        for l in range(w):
            if(mat[i-l][j+l] != p):
                break
            elif(l == w-1):
                s = p
for i in range(n-w+1):
    for j in range(m-w+1):
        p = mat[i][j]
        for l in range(w):
            if(mat[i+l][j+l] != p):
                break
            elif(l == w-1):
                s=p

#Horizontal
for i in range(n):
    for j in range(m-w+1):
        p = mat[i][j]
        for l in range(w):
            if(mat[i][j+l] != p):
                break
            elif(l == w-1):
                s=p
                   
#vertical
for i in range(n-w+1):
    for j in range(m):
        p = mat[i][j]
        for l in range(w):
            if(mat[i+l][j] != p):
                break
            elif(l == w-1):
                s=p
if s == -2:
    print(-1)
else:
    print(s)
    

