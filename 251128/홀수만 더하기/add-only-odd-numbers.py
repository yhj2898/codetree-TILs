n = int(input())
arr = [int(input()) for _ in range(n)]

total=0
for i in arr:
    if i%2==1 and i%3==0:
        total += i
print(total)
