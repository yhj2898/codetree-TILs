dirs = input()

# Please write your code here.
dx = [1,0,-1,0]
dy = [0,-1,0,1]
x, y = 0,0

dr=3

for i in dirs:
    if i == 'L':
        dr = (dr+3)%4
    elif i == 'R':
        dr = (dr+1)%4
    else:
        x+=dx[dr]
        y+=dy[dr]

print(x,y)