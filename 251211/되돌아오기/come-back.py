n = int(input())
dxs=[0,1,0,-1]
dys=[1,0,-1,0]
mapping={'E':0, 'S':1, 'W':2, 'N':3}
arr = [[0 * 2001] for _ in range(2001)]
x,y= 1000,1000
time=0
answer=-1
for _ in range(n):
    d, dist = input().split()
    dist = int(dist)
    dir = mapping[d]

    for _ in range(dist):
        x += dxs[dir]
        y += dys[dir]
        time +=1
        if x==1000 and y == 1000:
            answer = time
            break
    if answer != -1:
        break

print(answer)