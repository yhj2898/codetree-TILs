n = int(input())
a = [int(input()) for _ in range(n)]

import sys
ans = sys.maxsize

for i in range(n):
    dist=0
    for j in range(n):
        dist += abs((j-i+n)%n) * a[j]
    ans = min(ans,dist)
print(ans)