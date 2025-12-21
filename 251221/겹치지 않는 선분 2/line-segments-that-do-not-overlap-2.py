n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ans=0

for i, (x1,y1) in enumerate(lines):
    ok = True
    for j, (x2,y2) in enumerate(lines):
        if x1==x2 and y1==y2:
            continue
        if (x1-x2)*(y1-y2)<0:
            ok = False
            break
    if ok:
        ans+=1
print(ans)