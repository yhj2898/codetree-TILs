n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    x=1
    for i in range(a,b+1):
        x*=i
    print(x)