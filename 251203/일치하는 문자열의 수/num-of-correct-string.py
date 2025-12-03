n,a = input().split()
n=int(n)

arr = [input() for _ in range(n)]

cnt=0
for i in arr:
    if i == a:
        cnt+=1
print(cnt)