n=int(input())
arr = [int(input()) for _ in range(n)]

total=0
for i in arr:
    total += i

total = str(total)
print(total[1:] + total[0])