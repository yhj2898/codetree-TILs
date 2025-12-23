n, b = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
ans=0
for i in range(n):
    buget=gifts[i][0]//2 + gifts[i][1]
    cnt=0
    for j in range(n):
        if i==j:
            continue
        if buget>b:
            break
        buget += gifts[j][0] + gifts[j][1]
        cnt+=1
    ans = max(ans, cnt)
print(ans)
