arr = [int(input()) for _ in range(10)]

total = 0
cnt = 0
for i in arr:
    if 0<= i <=200:
        total +=i
        cnt +=1

print(f'{total} {total/cnt:.1f}')