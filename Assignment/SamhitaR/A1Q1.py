def check():
    x = -1
    for i in range (n): #checking rows
        for j in range (m-w+1):
            a = matrix[i][j]
            for l in range (j+1,j+w):
                if matrix[i][l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x
    for i in range (n-w+1): #checking columns
        for j in range (m):
            a = matrix[i][j]
            for l in range (i+1,i+w):
                if matrix[l][j] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x
    for i in range (n-1,w-2,-1): #checking positive diagonals
        for j in range (m-w+1):
            a = matrix[i][j]
            for l in range(1,w):
                if matrix[i-l][j+l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x   
    for i in range (n-1,w-2,-1): #checking negative diagonals
        for j in range (m-1,w-2,-1):
            a = matrix[i][j]
            for l in range(1,w):
                if matrix[i-l][j-l] != a:
                    x = -1
                    break
                else:
                    x = a
            if(x>-1):
                return x
    return x
n,m,k,w = map(int, input().split()) 
matrix = []
for i in range (n):
    s = input().split()
    s1 = []
    for j in range (m):
        s1.append(int(s[j]))
    matrix.append(s1)
print(check())

