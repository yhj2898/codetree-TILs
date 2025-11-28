a,b = [float(input()) for _ in range(2)]

if a>=1 and b>=1:
    print('High')
elif a>=0.5 and b>=0.5:
    print('Middle')
else:
    print('Low')