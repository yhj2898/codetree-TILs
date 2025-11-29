n=int(input())

x=2
for i in range(n):
    for j in range(n):
        print(x, end=' ')
        x+=2
        if x==10:
            x=2
    print()