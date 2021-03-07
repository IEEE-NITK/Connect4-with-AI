n,q = list(map(int,input().split()))
stacks = [[] for i in range(n)]
for i in range(q):
    query = list(map(int,input().split()))
    if(query[0] == 1):
        stacks[query[1]].append(query[2])
    elif(query[0] == 2):
        print(stacks[query[1]][-1])
        stacks[query[1]].pop()
    else:
        for j in range(n):
            if(len(stacks[j]) <= query[1]):
                print("1")
                break
            elif(j == n-1):
                print("0")