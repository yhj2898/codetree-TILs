import sys
ans=sys.maxsize

arr = list(map(int, input().split()))
n=len(arr)
def diff(a,b,c):
    sum1 = arr[a]+arr[b]
    sum2 = arr[c]
    sum3 = sum(arr) - sum1 - sum2
    if sum1 != sum2 and sum2 != sum3 and sum3 != sum1:
        return (max(sum1, sum2, sum3) - min(sum1, sum2, sum3))
    else:
        return sys.maxsize
        

for a in range(n):
    for b in range(a+1, n):
        for c in range(n):
            if a==c or b==c:
                continue
            ans = min(ans, diff(a,b,c))

if ans==sys.maxsize:
    print(-1)
else:
    print(ans)
