n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
while a:
    m=max(a)
    idx = a.index(m)
    print(idx+1, end=' ')
    a=a[:idx]
