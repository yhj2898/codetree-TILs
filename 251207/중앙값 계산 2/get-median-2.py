n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(0,n+1,2):
    arr[:i+1] = sorted(arr[:i+1])
    print(arr[:i+1][i//2], end=' ')