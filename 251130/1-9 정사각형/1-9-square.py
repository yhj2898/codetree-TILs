n=int(input())

cnt=1
for i in range(n):
    for j in range(n):
        print(cnt, end='')
        if cnt>=9:
            cnt-=8
        else:
            cnt+=1
    print()