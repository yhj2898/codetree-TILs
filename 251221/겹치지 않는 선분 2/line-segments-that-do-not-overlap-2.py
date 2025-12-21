n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

for i, (x1,y1) in enumerate(lines):
    cnt=0
    for j, (x2,y2) in enumerate(lines):
        if x1==x2 and y1==y2:
            continue
        if (x1-x2)*(y1-y2)>0:
            cnt+=1
print(cnt)