n=int(input())
arr=list(map(int,input().split()))

x = [0]*10

for i in arr:
    x[i] +=1

for i in range(1,10):
    print(x[i])