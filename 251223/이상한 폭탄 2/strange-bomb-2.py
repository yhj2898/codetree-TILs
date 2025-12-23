n,k = map(int, input().split())
num = [int(input()) for _ in range(n)]

ans=-1

for i in range(n):
    idx = []

    for j in range(i+1,n):
        if num[j]==num[i]:
            idx.append(j)
    if not idx:
        continue
    if idx[-1] - idx[0] <=k:
        ans = max(ans, num[i])
print(ans)