n = int(input())
arr = [int(input()) for _ in range(n)]

import sys
max_sum = -sys.maxsize

def no_carry(a,b,c):
    a,b,c = str(a), str(b), str(c)
    i,j,k = len(a)-1, len(b)-1, len(c)-1

    while i>=0 or j>=0 or k>=0:
        aa = int(a[i]) if i>=0 else 0
        bb = int(b[j]) if j>=0 else 0
        cc = int(c[k]) if k>=0 else 0
        if aa + bb + cc >= 10:
            return False
        i-=1
        j-=1
        k-=1
    return True
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if no_carry(arr[i],arr[j],arr[k]):
                ans = max(ans, arr[i]+arr[j]+arr[k])
print(ans)