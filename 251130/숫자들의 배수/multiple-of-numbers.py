n=int(input())
arr=[]

cnt=0
for i in range(1,100):
    arr.append(n*i)
    if i%5==0:
        cnt+=1
    if cnt==2:
        break

for i in arr:
    print(i, end=' ')
