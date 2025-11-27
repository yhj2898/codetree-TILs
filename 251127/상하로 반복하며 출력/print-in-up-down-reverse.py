n = int(input())
arr =[[0 for _ in range(n)] for _ in range(n)]

for j in range(n):
    if j%2 ==0:
        for i in range(n):
            arr[i][j] = i+1
    else:
        for i in range(n-1,-1,-1):
            arr[i][j] = n-i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()
