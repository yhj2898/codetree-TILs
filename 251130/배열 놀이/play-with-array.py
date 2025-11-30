n,q = map(int,input().split())
arr = list(map(int, input().split()))

for i in range(q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        print(arr[x[1]-1])
    elif x[0] == 2:
        print(arr.index(x[1])+1 if True else 0)
    elif x[0] ==3:
        print(' '.join(map(str,arr[x[1]-1:x[2]])))