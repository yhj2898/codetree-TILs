n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

ans=0
operating_time=0
for i in range(n):
    t = [0]* 1001
    for j, (x,y) in enumerate(times):
        if i==j:
            continue
        for k in range(x, y):
            t[k]+=1
    operating_time = sum(1 for l in range(1001) if t[l]>0)
    ans = max(ans, operating_time)
print(ans)