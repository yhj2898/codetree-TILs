n = int(input())
A = list(map(int, input().split()))

import sys
min_sum = sys.maxsize

for i in range(n):
    total=0
    for j in range(n):
        total += A[j]*abs(i-j)
    min_sum=min(min_sum,total)
print(min_sum)