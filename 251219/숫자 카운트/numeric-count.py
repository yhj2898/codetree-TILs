n = int(input())
q = []
candidates=[]
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    q.append((str(num),cnt1,cnt2))

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i!=j and j!=k and k!=i:
                candidates.append([str(i),str(j),str(k)])
def guess(A):
    for B, c1, c2 in q:
        strike=0
        ball=0

        for p in range(3):
            if A[p] == B[p]:
                strike +=1
            elif A[p] in B:
                ball +=1
        
        if strike != c1 or ball != c2:
            return False
    return True
            

ans=0
for A in candidates:
    if guess(A):
        ans+=1
print(ans)