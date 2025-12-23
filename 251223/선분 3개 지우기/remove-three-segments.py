n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
x = [0]*101
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            remain=[]
            for idx in range(n):
                if idx!=i and idx!=j and idx!=k:
                    remain.append(lines[idx])
            
            cond = True
            for a in range(n-3):
                for b in range(a+1, n-3):
                    x1, y1 = remain[a]
                    x2, y2 = remain[b]

                    if not (y1<x2 or y2<x1):
                        cond = False
                        break
                if not cond:
                    break
            if cond:
                ans+=1
print(ans)
