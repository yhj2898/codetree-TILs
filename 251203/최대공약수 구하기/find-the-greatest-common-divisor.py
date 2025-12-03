n, m = map(int, input().split())

# Please write your code here.
def max_div(n,m):
    x = []
    if n>m:
        for i in range(2,m):
            if n%i==0:
                x.append(i)
    else:
        for i in range(2,n):
            if n%i==0:
                x.append(i)
    print(max(x))

max_div(n,m)