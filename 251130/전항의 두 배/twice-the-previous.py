a,b=map(int,input().split())
arr=[0 for _ in range(10)]

arr[0]=a
arr[1]=b

for i in range(2,10):
    arr[i] = arr[i-1] + 2*arr[i-2]

for i in arr:
    print(i, end=' ')