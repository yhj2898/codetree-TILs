n = int(input())
numbers = list(map(int, input().split()))

import sys
max_sum = -sys.maxsize
total=0
for i in range(n):
    for j in range(n):
        if abs(i-j) == 1 or i==j:
            continue
        total = numbers[i]+numbers[j]
        max_sum = max(max_sum, total)
print(max_sum) 
        

        