n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1], f(arr,n-1))

print(f(arr,n))