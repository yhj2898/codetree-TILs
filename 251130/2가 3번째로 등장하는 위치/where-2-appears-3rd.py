n=int(input())
arr = list(map(int,input().split()))

cnt=0
idx=0
for i in arr:
    idx+=1
    if i==2:
        cnt+=1
    if cnt==3:
        print(idx)
        break