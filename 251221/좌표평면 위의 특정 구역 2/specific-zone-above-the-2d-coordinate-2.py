n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

import sys
ans = sys.maxsize

for i in range(n):
    min_x, min_y = sys.maxsize,sys.maxsize
    max_x, max_y = -sys.maxsize, -sys.maxsize

    for j in range(n):
        if i==j:
            continue
        x, y = points[j]
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)

    area = (max_x-min_x)*(max_y-min_y)
    ans = min(ans,area)
print(ans)