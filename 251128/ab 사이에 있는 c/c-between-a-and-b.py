a,b,c =map(int,input().split())

x = False

for i in range(a,b+1):
    if i%c==0:
        x = True

if x:
    print('YES')
else:
    print('NO')