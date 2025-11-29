n=int(input())
for i in range(1,n+1):
    for j in range(1,n):
        print(f'{i} * {j} = {i*j}', end=', ')
    for j in range(n,n+1):
        print(f'{i} * {j} = {i*j}')