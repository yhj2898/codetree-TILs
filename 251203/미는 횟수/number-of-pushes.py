a = input()
b = input()

cnt=0
for i in range(len(a)):
    if a==b:
        print(cnt)
        break
    else:
        a = a[-1] + a[:-1]
        cnt+=1
else:
    print(-1)