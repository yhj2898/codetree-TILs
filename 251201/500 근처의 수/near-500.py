arr=list(map(int,input().split()))

a = []
b = []

for n in arr:
    if n<500:
        a.append(n)
    else:
        b.append(n)

print(max(a), min(b), end=' ')