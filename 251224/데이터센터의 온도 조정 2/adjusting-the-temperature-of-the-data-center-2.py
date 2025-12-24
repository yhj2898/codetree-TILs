N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

def work(i,a,b):
    if i<a:
        return C
    elif a<=i<=b:
        return G
    else:
        return H

max_total=0
for i in range(1001):
    total=0
    for a,b in ranges:
        total += work(i,a,b)
    max_total = max(max_total,total)
print(max_total)
