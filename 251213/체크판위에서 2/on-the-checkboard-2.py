r,c = map(int, input().split())
a = [list(input().split()) for _ in range(r)]

cnt=0
for i in range(1,r-2):
    for j in range(1,c-2):
        for k in range(i+1, r-1):
            for l in range(j+1,c-1):
                if a[0][0] != a[i][j] and a[i][j] != a[k][l] and a[k][l]!=a[r-1][c-1]:
                    cnt+=1
print(cnt)   
    