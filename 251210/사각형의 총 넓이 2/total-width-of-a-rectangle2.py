n = int(input())
offset = 100
a = [[0]*201 for _ in range(201)]
cur = offset
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1+=100
    y1+=100
    x2+=100
    y2+=100

    for i in range(x1,x2):
        for j in range(y1,y2):
            a[i][j]=1

total =0
for i in a:
    for j in i:
        if j==1:
            total+=1
print(total)


