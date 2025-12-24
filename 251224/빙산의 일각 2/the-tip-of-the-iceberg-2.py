n = int(input())
h = [int(input()) for _ in range(n)]

ans=0
for k in range(1001):
    arr=[0]*(n+1)
    cnt=0
    for i in range(n):
        arr[i] = 1 if h[i]>k else -1
        
    for i in range(n-1):
        if arr[i]*arr[i+1]==-1:
            cnt+=1
    ans = max(ans, cnt//2+1)
print(ans)
    