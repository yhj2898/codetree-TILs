n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]

cnt=1
for d in range(n+m-1):
    for i in range(n):
        j = d-i
        if 0<=j<m:
            arr[i][j] = cnt
            cnt+=1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()