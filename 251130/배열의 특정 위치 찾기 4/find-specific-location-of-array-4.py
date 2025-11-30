arr =list(map(int, input().split()))
ans=[]
for i in arr:
    if i==0:
        break
    if i%2==0:
        ans.append(i)

print(len(ans), sum(ans))