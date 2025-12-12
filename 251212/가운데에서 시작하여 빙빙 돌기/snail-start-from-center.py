n = int(input())
answer = [[0] * n for _ in range(n)]

dxs=[0,-1,0,1]
dys=[1,0,-1,0]
x, y = (n-1)//2, (n-1)//2
dn=0
answer[x][y]=1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

# 1,1,2,2,3,3,4,4
step=1
cnt=0
num=2

while num<=n*n:
    for _ in range(step):
        if num>n*n:
            break
        x+=dxs[dn]
        y+=dys[dn]
        answer[x][y]=num
        num+=1
        
    dn = (dn+1)%4
    cnt+=1
    if cnt==2:
        step+=1
        cnt=0

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()