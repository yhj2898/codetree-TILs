n, m = map(int, input().split())

# Please write your code here.
def f(n,m):
    answer=0
    for i in range(max(m,n),m*n):
        if i%n==0 and i%m==0:
            answer = i
            break
    print(answer)

f(n,m)
