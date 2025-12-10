n = int(input())
offset = 100000
a = [0] * (2*offset+1)
cnt_w = [0] * (2*offset+1)
cnt_b = [0] * (2*offset+1)
w,b,g = 0,0,0

cur = offset
for _ in range(n):
    x,d = input().split()
    x = int(x)

    if d=='L':
        while x>0:
            a[cur] = 'w'
            cnt_w[cur] +=1
            x-=1
            if x:
                cur-=1
    else:
        while x>0:
            a[cur]='b'
            cnt_b[cur]+=1
            x-=1
            if x:
                cur+=1

for i in range(len(a)):
    if cnt_w[i]>=2 and cnt_b[i]>=2:
        g+=1
    elif a[i]=='w':
        w+=1
    elif a[i]=='b':
        b+=1
print(w,b,g)