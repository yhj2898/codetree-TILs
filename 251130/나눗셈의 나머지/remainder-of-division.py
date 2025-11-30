a,b=map(int,input().split())

x=[0] * 10

while True:
    if a<=1:
        break
    x[a%b] +=1
    a//=b

total=0
for i in x:
    total += i**2
print(total)