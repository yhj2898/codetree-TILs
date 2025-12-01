n=int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

cnt=1
if n%2==0:
    for col in range(n-1,-1,-1):
        if col %2==0:
            for row in range(n):
                a[row][col] = cnt
                cnt+=1
        else:
            for row in range(n-1,-1,-1):
                a[row][col] = cnt
                cnt+=1
else:
    for col in range(n-1,-1,-1):
        if col %2==0:
            for row in range(n-1,-1,-1):
                a[row][col] = cnt
                cnt+=1
        else:
            for row in range(n):
                a[row][col] = cnt
                cnt+=1

for i in a:
    for j in i:
        print(j, end=' ')
    print()