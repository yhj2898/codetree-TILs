n=int(input())
cnt=0
for _ in range(n):
    x=list(map(int,input().split()))
    if sum(x)/len(x) >=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
    
print(cnt)