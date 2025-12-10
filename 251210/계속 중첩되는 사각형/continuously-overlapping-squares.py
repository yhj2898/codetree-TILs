n=int(input())
offset = 1000
rects = [tuple(map(int, input().split())) for _ in range(n)]
c = [[0]*(2*offset+1) for _ in range((2*offset+1))]

for i, (x1,y1,x2,y2) in enumerate(rects, start=1):
    if i%2==1:
        for x in range(x1,x2):
            for y in range(y1, y2):
                c[x][y]='r'
    else:
        for x in range(x1,x2):
            for y in range(y1,y2):
                c[x][y]='b'

area=0
for x in range(len(c)):
    for y in range(len(c)):
        if c[x][y]=='b':
            area+=1
print(area)