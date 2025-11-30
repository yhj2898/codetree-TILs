arr=list(map(int, input().split()))
ans=[]

for i in arr:
    if i==0:
        break
    ans.append(i)

ans = ans[::-1]

for i in ans:
    print(i, end=' ')