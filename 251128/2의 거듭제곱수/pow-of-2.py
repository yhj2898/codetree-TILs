n=int(input())
x=0
while True:
    if 2**x==n:
        break
    x+=1
print(x)