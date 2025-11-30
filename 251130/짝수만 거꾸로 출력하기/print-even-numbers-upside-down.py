n=int(input())
arr=list(map(int, input().split()))
ans=[]

for i in arr:
    if i%2==0:
        ans.append(i)

ans = ans[::-1]

for i in ans:
    print(i, end=' ')