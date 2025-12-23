n, b = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
ans=0
for i in range(n):
    costs = []

    for j in range(n):
        if i==j:
            costs.append(gifts[j][0]//2+gifts[j][1])
        else:
            costs.append(gifts[j][0]+gifts[j][1])
    costs.sort()

    total = 0
    cnt=0
    for c in costs:
        if total + c > b:
            break
        total+=c
        cnt+=1
    ans = max(ans,cnt)
print(ans)