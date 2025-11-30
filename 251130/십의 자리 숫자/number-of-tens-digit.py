arr = list(map(int, input().split()))
x=[0]*10

for i in arr:
    x[i//10] +=1

for i in range(1,10):
    print(f'{i} - {x[i]}')
