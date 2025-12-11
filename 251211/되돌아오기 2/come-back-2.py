commands = input()

dxs=[1,0,-1,0]
dys=[0,-1,0,1]
x,y = 0,0
dir = 3
ans=-1
time=0
for i in commands:
    if i=='L':
       dir = (dir+3)%4
       time+=1
    elif i=='R':
        dir = (dir+1)%4
        time+=1
    else:
        x += dxs[dir]
        y += dys[dir]
        time+=1
    
    if x==0 and y==0:
        ans = time
        break
print(ans)