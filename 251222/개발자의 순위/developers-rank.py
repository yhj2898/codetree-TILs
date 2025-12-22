k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

rank = []
for game in arr:
    temp = [0] * (n+1)
    for idx, p in enumerate(game):
        temp[p] = idx
    rank.append(temp)

cnt=0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            continue
        cond = True
        for i in range(k):
            if rank[i][a] > rank[i][b]:
                cond= False
                break
        if cond:
            cnt+=1
print(cnt)