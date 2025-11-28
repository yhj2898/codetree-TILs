a,b,c = map(int, input().split())

if a<=b:
    if c<a:
        print(a)
    elif c>b:
        print(b)
    else:
        print(c)
else:
    if c>a:
        print(a)
    elif c<b:
        print(b)
    else:
        print(c)