A, B, C = map(int, input().split())

ans=0
for i in range(1000):
    for j in range(1000):
        total = A*i + B*j
        if total<=C:
            ans=max(ans,total)
            
print(ans)    