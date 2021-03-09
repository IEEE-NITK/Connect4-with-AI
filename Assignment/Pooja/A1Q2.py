N, Q =  [int(x) for x in input("Enter the number of stacks anf quires: ").split()]
s = []
count=0
for k in range(1,N+1):
    s.append([])

while Q !=0:
    l1= []
    l1= list(map(int,input("Enter the values: ").strip().split(' ')))[:3]
    if l1[0]==1:# query no 1
        stack=s[l1[1]]
        stack.append(l1[2])
    elif l1[0]==2:#query no 2
        stack=s[l1[1]]
        print(stack.pop())
    elif l1[0]==3:#query no 3
        for i in range(0,N):
            if len(s[i])<=l1[1]:
                count = 0
                count = count+1
        if count == 0:
            print("0")
        else:
            print("1")
    Q=Q-1
    count = 0
    
        


