n = int(input())

prime=[]

for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0:
    prime.append(i)
print(prime)