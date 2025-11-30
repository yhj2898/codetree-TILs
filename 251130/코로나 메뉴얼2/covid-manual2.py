x=[0]*4
for i in range(3):
    si, ti = input().split()
    ti = int(ti)
    if si=='Y' and ti>=37:
        x[0]+=1
    elif si=='N' and ti>=37:
        x[1]+=1
    elif si=='Y' and ti<37:
        x[2]+=1
    else:
        x[3]+=1
for i in x:
    print(i,end=' ')

if x[0]>=2:
    print('E')
