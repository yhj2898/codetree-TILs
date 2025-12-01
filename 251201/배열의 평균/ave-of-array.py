arr = [list(map(int,input().split())) for _ in range(2)]


total3=0

for i in range(2):
    total1=0
    for j in range(4):
        total1 += arr[i][j]
    print(f'{total1/4:.1f}',end=' ')
print()

for i in range(4):
    total2=0
    for j in range(2):
        total2 += arr[j][i]
    print(f'{total2/2:.1f}',end=' ')
print()
total3=0
for i in range(2):
    for j in range(4):
        total3 += arr[i][j]
print(f'{total3/8:.1f}')
