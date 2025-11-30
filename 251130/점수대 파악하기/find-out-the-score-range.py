arr = list(map(int, input().split()))
x = [0] *10

for i in range(10,0,-1):
    cnt=0
    for elem in arr:
        if elem==0:
            break
        if elem//10 ==i:
            cnt+=1
    print(f'{i*10} - {cnt}')