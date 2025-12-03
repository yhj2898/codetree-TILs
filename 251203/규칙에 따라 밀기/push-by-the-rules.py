a=input()
x = input()

for i in x:
    if i=='L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]
    
print(a)