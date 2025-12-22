n, b = map(int, input().split())
p = [int(input()) for _ in range(n)]

ans=0

for i in range(n):
    budget = b - p[i]//2
    cnt = 1

    others=[]
    for j in range(n):
        if i!=j:
            others.append(p[j])
    others.sort()

    for price in others:
        if budget>=price:
            budget -=price
            cnt+=1
        else:
            break
    ans = max(ans, cnt)
print(ans)