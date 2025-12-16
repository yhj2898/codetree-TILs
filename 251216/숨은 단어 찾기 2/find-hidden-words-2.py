n, m = map(int, input().split())
arr = [input() for _ in range(n)]

dxs, dys = [1,1,1,-1,-1,-1,0,0], [-1,0,1,-1,0,1,-1,1]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

cnt=0
for i in range(n):
    for j in range(m):
        if arr[i][j]!='L':
            continue
        for dx, dy in zip(dxs, dys):
            x,y = i,j
            if in_range(x+2*dx,y+2*dy)==True and arr[x+dx][y+dy]=='E' and arr[x+2*dx][y+2*dy]=='E':
                cnt+=1
print(cnt)
