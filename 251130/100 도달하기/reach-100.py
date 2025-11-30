n=int(input())
arr=[1,n]

for i in range(2,100):
    arr.append(arr[i-1] + arr[i-2])
    if arr[i]>100:
        break

for i in arr:
    print(i, end=' ')