n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx = [0,1,-1,0]
dy = [1,0,0,-1]
dn={'R':0, 'D':1, 'U':2, 'L':3}
dir = dn[d]
x,y = r-1, c-1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for _ in range(t):
    nx, ny = x+dx[dir], y+dy[dir]
    if not in_range(nx, ny):
        dir = 3-dir
        nx, ny = x+dx[dir], y+dy[dir]
    else:
        x, y = nx, ny

print(x+1, y+1)
