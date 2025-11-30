arr = list(map(int, input().split()))
ans=[]
for i in arr:
    if i==999 or i==(-999):
        break
    ans.append(i)
print(max(ans), min(ans))    