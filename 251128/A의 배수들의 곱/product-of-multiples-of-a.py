a,b = map(int, input().split())

m=1
for i in range(1,b+1):
    if i%a==0:
        m *= i
print(m)