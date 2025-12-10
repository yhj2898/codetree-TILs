n = int(input())
x,y = 0,0
for _ in range(n):
    d, r = input().split()
    r=int(r)

    if d=='W':
        x-=r
    elif d=='E':
        x +=r
    elif d=='S':
        y -=r
    else:
        y+=r

print(x,y)
