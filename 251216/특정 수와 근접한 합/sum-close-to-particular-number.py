n, s = map(int, input().split())
arr = list(map(int, input().split()))

import sys
min_diff = sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        total=sum(arr)-arr[i]-arr[j]
        min_diff = min(min_diff, abs(total-s))
print(min_diff)