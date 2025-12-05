n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def dev_even(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i] //= 2
    for i in arr:
        print(i, end=' ')

dev_even(arr)

