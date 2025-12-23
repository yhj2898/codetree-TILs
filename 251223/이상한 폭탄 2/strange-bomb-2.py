n,k = map(int, input().split())
num = [int(input()) for _ in range(n)]

ans=-1
idx=[]
for i in range(n):
    idx=[i]
    for j in range(i+1,n):
        if num[j]==num[i]:
            idx.append(j)
    if not idx:
        continue
    if len(idx)>=2 and idx[-1] - idx[0] <=k:
        ans = max(ans, num[i])
print(ans)