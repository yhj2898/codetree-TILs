offset = 1000
recs = [tuple(map(int, input().split())) for _ in range(2)]
c = [[0] * (2*offset+1) for _ in range(2*offset+1)]

for i, (x1, y1, x2, y2) in enumerate(recs, start=1):
    x1, y1 = x1+offset, y1+offset
    x2, y2 = x2+offset, y2+offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            c[x][y] = i

xs=[]
ys=[]

for x in range(len(c)):
    for y in range(len(c)):
        if c[x][y]==1:
            xs.append(x)
            ys.append(y)
if len(xs) == 0:
    print(0)
else:
    print((max(xs)-min(xs)+1) * (max(ys)-min(ys)+1))

