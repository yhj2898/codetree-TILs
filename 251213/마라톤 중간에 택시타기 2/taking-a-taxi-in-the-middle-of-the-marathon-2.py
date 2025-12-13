import sys

n=int(input())
points = [list(map(int, input().split())) for _ in range(n)]

min_dist = sys.maxsize
total=0
cur=0
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for i in range(n-1):
    total += dist(points[i],points[i+1])

for i in range(1,n-1):
    cur = total
    cur -= dist(points[i-1],points[i])
    cur -= dist(points[i],points[i+1])
    cur += dist(points[i-1],points[i+1])
    min_dist = min(min_dist, cur)

print(min_dist)