n, q = map(int, input().split())
stacks = []
for i in range (n):
    stacks.append([])
while(q):
    s = input().split()
    if s[0] == '1':
        i = int(s[1])
        el = int(s[2])
        stacks[i].append(el)
    elif s[0] == '2':
        i = int(s[1])
        print(stacks[i].pop())
    elif s[0] == '3':
        m = int(s[1])
        b = 0
        for i in range (n):
            if(len(stacks[i]) <= m):
                b = 1
                break
        print(b)
    q -= 1
