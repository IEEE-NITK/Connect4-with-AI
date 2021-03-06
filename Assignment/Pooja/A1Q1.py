s = input("").split(" ")
N = int(s[0]); M = int(s[1]); K = int(s[2]); W = int(s[3])
matrix = []
for i in range(N):
    sub_matrix = input("").split(" ")
    for j in range(len(sub_matrix)):
        sub_matrix[j] = int(sub_matrix[j])
    matrix.append(sub_matrix)
transpose_matrix = []
for i in range(M):
    c = []
    for j in range(N):
        c.append(0)
    transpose_matrix.append(c)
for j in range(len(matrix)):
    for i in range(len(matrix[0])):
        transpose_matrix[i][j] = matrix[j][i]
diagonal_matrix = []
a = []
b = []
for i in range(min(M,N)):
    b.append(matrix[i][i])
    a.append(matrix[i][M-i-1])
diagonal_matrix.append(a)
diagonal_matrix.append(b)
combined = matrix + transpose_matrix + diagonal_matrix
result = []
for i in combined:
    for j in (range(len(i)-W + 1)):
        result.append(list(i[j:j+W]))
s = 0
for i in result:
    if len(set(i)) == 1:
        print(i[0])
        s += 1
        break
if s == 0:
    print(-1)