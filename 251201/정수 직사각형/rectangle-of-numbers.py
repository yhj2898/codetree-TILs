n,m=map(int,input().split())

cnt=0
for i in range(n):
    for j in range(m):
        cnt+=1
        print(cnt, end=' ')
    print()