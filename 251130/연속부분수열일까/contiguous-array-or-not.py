n1, n2 = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

cond=False
for i in range(n1):
    for j in range(n1):
        if arr1[i:j+1] == arr2:
            cond=True
if cond:
    print('Yes')
else:
    print('No')
            