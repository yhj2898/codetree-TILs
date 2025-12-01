a,b=input().split()

if len(a)>len(b):
    print(a, len(a), end=' ')
elif len(a)<len(b):
    print(b, len(b), end=' ')
else:
    print('same')