n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def f(m):
    list_m=[m]
    while m!=1:
        if m%2==1: 
            m -=1
        else:
            m //=2
        list_m.append(m)
    return list_m

total=0
for i in range(n):
    for j in f(m):
        if i==j-1:
            total += A[i]
print(total)