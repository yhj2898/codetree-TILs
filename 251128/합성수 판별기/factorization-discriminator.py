n= int(input())

h=False

for i in range(2,n):
    if n%i==0:
        h=True

if h:
    print('C')
else:
    print('N')