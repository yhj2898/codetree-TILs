n=int(input())
arr = list(map(int, input().split()))

min_val=999
for i in arr:
    for j in arr:
        if i<=j:
            continue
        if i-j<min_val:
            min_val = i-j
            
print(min_val)