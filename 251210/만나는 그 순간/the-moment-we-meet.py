n, m = map(int, input().split())

a = []
b = []

cur =0
for _ in range(n):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'R':
            cur +=1
        else:
            cur -=1
        a.append(cur)

cur=0
for _ in range(m):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'R':
            cur+=1
        else:
            cur-=1
        b.append(cur)

for i in range(min(len(a), len(b))):
    if a[i]==b[i]:
        print(i+1)
        break
else:
    print(-1)