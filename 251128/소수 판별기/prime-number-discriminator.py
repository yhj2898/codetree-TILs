n=int(input())
prime = True

for i in range(2,n-1):
    if n%i==0:
        prime=False
    
if prime is True:
    print('P')
else:
    print('C')