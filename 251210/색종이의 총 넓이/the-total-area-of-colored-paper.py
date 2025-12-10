n = int(input())
offset = 100
c = [[0] * (2*offset+1) for _ in range(2*offset+1)]

for _ in range(n):
    x1, y1 = map(int, input().split())
    
    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            c[x][y]=1
area=0
for x in range(len(c)):
    for y in range(len(c)):
        if c[x][y]==1:
            area+=1

print(area)