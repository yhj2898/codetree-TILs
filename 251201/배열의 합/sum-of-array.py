arr=[list(map(int,input().split())) for _ in range(4)]


for i in arr:
    total=0
    for j in i:
       total+=j
    print(total) 