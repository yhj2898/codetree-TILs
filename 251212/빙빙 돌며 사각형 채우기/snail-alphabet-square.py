n, m = map(int, input().split())
answer = [[0]*m for _ in range(n)]
dxs=[0,1,0,-1]
dys=[1,0,-1,0]
x,y=0,0
dn=0
answer[x][y]=ord('A')

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for i in range(2,n*m+1):
    nx, ny = x + dxs[dn], y + dys[dn]
    if not in_range(nx,ny) or answer[nx][ny]!=0:
        dn = (dn+1)%4
    x, y = x + dxs[dn], y + dys[dn]
    answer[x][y]=ord('A')+(i-1)%26

for i in range(n):
    for j in range(m):
        print(chr(answer[i][j]), end=' ')
    print()

