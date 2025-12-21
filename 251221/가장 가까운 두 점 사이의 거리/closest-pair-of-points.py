n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

import sys
ans=sys.maxsize

for i,(x1,y1) in enumerate(points):
    for j,(x2,y2) in enumerate(points):
        if i==j:
            continue
        dist = (x1-x2)**2 + (y1-y2)**2
    ans = min(ans, dist)
print(ans)