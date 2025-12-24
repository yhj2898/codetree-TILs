n = int(input())
h = [int(input()) for _ in range(n)]

ans=0
for k in range(1001):
    cnt=0
    for i in range(n):
        if h[i]>k and (i==0 or h[i-1]<=k):
            cnt+=1
    ans=max(ans,cnt)
print(ans)