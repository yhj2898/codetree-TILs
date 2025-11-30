arr=list(map(int, input().split()))

total=0
for i in range(1,10,2):
    total += arr[i]
print(total, end=' ')

total=0
cnt=0
for i in range(2,10,3):
    total += arr[i]
    cnt +=1
print(f'{total/cnt:.1f}')