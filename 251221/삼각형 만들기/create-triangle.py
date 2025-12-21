n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans=0
for x1, y1 in points:
    base = 0
    height = 0
    for x2, y2 in points:
        if x1==x2:
            base = max(base, abs(y1-y2))
        if y1==y2:
            height = max(height, abs(x1-x2))
    ans = max(ans, base*height)
print(ans)