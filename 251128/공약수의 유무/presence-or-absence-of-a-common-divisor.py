a,b = map(int,input().split())

x=False
for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        x = True

if x:
    print(1)
else:
    print(0)