import sys

n = int(input())
arr = list(map(int, input().split()))

min_diff=sys.maxsize
for i in range(n):
    arr[i]*=2
    for j in range(n):
        remain=[]
        for k in range(n):
            if j!=k:
                remain.append(arr[k])
        
        sum_diff=0
        for k in range(n-2):
            sum_diff+= abs(remain[k]-remain[k+1])
        min_diff = min(min_diff,sum_diff)
    arr[i]//=2

print(min_diff)

