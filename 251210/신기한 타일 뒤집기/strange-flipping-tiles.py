n=int(input())
offset = 100000
a = [0] * (2*offset+1)
cur = offset
w, b = 0,0

for _ in range(n):
    x,d = input().split()
    x=int(x)

    if d=='L':
        while x>0:
            a[cur] = 'w'
            x-=1
            if x:
                cur-=1
    else:
        while x>0:
            a[cur] = 'b'
            x-=1
            if x:
                cur +=1

for i in range(len(a)):
    if a[i]=='w':
        w+=1
    elif a[i]=='b':
        b+=1

print(w,b)