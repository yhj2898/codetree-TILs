n, t = map(int, input().split())
c = input()
arr = [list(map(int, input().split())) for _ in range(n)]
dxs=[-1,0,1,0]
dys=[0,1,0,-1]
dn=0
x,y=n//2, n//2
answer = arr[x][y]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in c:
    if i=='L':
        dn = (dn+3)%4
    elif i=='R':
        dn = (dn+1)%4
    else:
        nx, ny = x+dxs[dn], y+dys[dn]
        if in_range(nx,ny):
            x, y = nx, ny
            answer += arr[x][y]

print(answer)