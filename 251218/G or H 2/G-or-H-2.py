n = int(input())
arr = [0] * 101
for i in range(n):
    d, a = input().split()
    d = int(d)
    arr[d] = a

idx = []
answer=0
for i in range(101):
    if arr[i]!=0:
        idx.append(i)

for i in range(len(idx)):
    for j in range(i, len(idx)):
        left = idx[i]
        right = idx[j]
        g=0
        h=0
       
        for k in range(left, right+1):
            if arr[k]=='G':
                g+=1
            elif arr[k]=='H':
                h+=1
        if g==0 or h==0 or g==h:
            answer = max(answer, right-left)
print(answer)