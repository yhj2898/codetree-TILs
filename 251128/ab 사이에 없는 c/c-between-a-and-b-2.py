a,b,c = map(int,input().split())

x=True
for i in range(a,b+1):
    if i%c==0:
        x=False
if x is False:
    print('NO')
else:
    print('YES')
