arr=list(map(int,input().split()))
ans=[]

for i in arr:
    if i==0:
        break
    else:
        ans.append(i)
print(ans[-1] + ans[-2] + ans[-3])