n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
clean = [0] * (n+1)

for a,b in commands:
    for i in range(a,b+1):
        clean[i]+=1

print(max(clean))