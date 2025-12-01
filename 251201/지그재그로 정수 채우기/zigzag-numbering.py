n, m = map(int, input().split())
arr=[[0 for _ in range(m)] for _ in range(n)]
# Please write your code here.
cnt=0
for j in range(m):
    if j%2==0:
        for i in range(n):
            arr[i][j] = cnt
            cnt+=1
    else:
        for i in range(n-1,-1,-1):
            arr[i][j] = cnt
            cnt+=1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()