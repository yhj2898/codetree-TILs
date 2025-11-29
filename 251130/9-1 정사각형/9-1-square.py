n=int(input())

x=9
for _ in range(n):
    for _ in range(n):
        print(x, end='')
        x-=1
        if x==0:
            x=9
    print()
