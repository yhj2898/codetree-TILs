arr=list(map(int, input().split()))
ans=[]

for i in arr:
    if i==0:
        break
    ans.append(i)

total = sum(ans)
avg = sum(ans)/len(ans)

print(total, f'{avg:.1f}')