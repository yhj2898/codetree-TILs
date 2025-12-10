offset = 1000
recs = [tuple(map(int, input().split())) for _ in range(2)]
c = [[0] * (2*offset+1) for _ in range(2*offset+1)]

for i, (x1, y1, x2, y2) in enumerate(recs, start=1):
    x1, y1 = x1+offset, y1+offset
    x2, y2 = x2+offset, y2+offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            c[x][y] = i

min_x, min_y = 9999,9999
max_x, max_y = -9999, -9999

for x in range(len(c)):
    for y in range(len(c)):
        if c[x][y]==1:
            if x<min_x: min_x = x
            if x>max_x: max_x = x
            if y<min_y: min_y = y
            if y>max_y: max_y = y

if min_x == 9999:
    print(0)
else:
    print((max_x-min_x+1) * (max_y-min_y+1))