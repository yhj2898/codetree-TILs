n = int(input())
arr = list(map(int, input().split()))

cnt=0
for i in range(n):
    for j in range(i,n):
        total=0
        for k in range(i,j+1):
            total+=arr[k]
        avg = total/(j-i+1)
        for k in range(i,j+1):
            if arr[k]==avg:
                cnt+=1
                break
print(cnt)