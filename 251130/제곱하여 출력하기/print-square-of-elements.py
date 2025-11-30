n=int(input())
arr=list(map(int, input().split()))

ans=[i**2 for i in arr]
for i in ans:
    print(i, end=' ')