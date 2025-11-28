n=int(input())
arr = [int(input()) for _ in range(n)]

total = 0
cnt = 0

for i in arr:
    total +=i
    cnt +=1

print(f'{total} {total/cnt:.1f}')