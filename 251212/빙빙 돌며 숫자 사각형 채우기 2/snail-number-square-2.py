n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
dxs=[1,0,-1,0]
dys=[0,1,0,-1]
x,y=0,0
dn = 0
arr[x][y]=1

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for i in range(2,n*m+1):
    nx, ny = x+dxs[dn], y+dys[dn]
    if not in_range(nx, ny) or arr[nx][ny] !=0:
        dn = (dn+1)%4
    x, y = x+dxs[dn], y + dys[dn]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()