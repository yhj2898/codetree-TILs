n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

import sys
min_sum=sys.maxsize

for i in range(n-t+1):
    total=0
    for j in range(i,i+t):
        total+=abs(arr[j]-h)
    min_sum = min(min_sum, total)
print(min_sum)