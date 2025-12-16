n, k = map(int, input().split())
arr = list(map(int, input().split()))

import sys
max_val = -sys.maxsize
for i in range(n-k+1):
    total=0
    for j in range(i, i+k):
        total+=arr[j]
    max_val = max(max_val, total)
print(max_val)
