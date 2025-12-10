offset = 1000
checked=[[0]*(2*offset+1) for _ in range(2*offset+1)]

for _ in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for x in range(x1,x2):
        for y in range(y1,y2):
            checked[x][y]=1

x1, y1, x2, y2 = tuple(map(int, input().split()))
for x in range(x1, x2):
    for y in range(y1, y2):
        checked[x][y]=0
area=0
for x in range(len(checked)):
    for y in range(len(checked)):
        if checked[x][y]==1:
            area+=1
print(area)