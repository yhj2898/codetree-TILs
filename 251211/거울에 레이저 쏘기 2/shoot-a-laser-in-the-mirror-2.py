n = int(input())
arr = [input() for _ in range(n)]

start = int(input())

# 주어진 숫자에 따른 시작위치와 방향 구하기(x, y, next_dir)
def initial(num):
    if num<=n:
        return 0, num-1, 0 
    elif num<=2*n:
        return num-n-1, n-1, 1 
    elif num<=3*n:
        return n-1, 3*n-num,2
    else:
        return 4*n-num, 0, 3

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def move(x,y,next_dir):
    dxs, dys = [1,0,-1,0], [0,-1,0,1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir

def simulate(x,y,dir):
    move_num=0
    while in_range(x,y):
        if arr[x][y] == '/':
            x, y, dir = move(x,y,dir ^ 1)
        else:
            x, y, dir = move(x,y,3-dir)
        move_num+=1
    return move_num

x,y,dir = initial(start)
move_num = simulate(x,y,dir)
print(move_num)