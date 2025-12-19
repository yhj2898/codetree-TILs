x = list(map(int, input().split()))

x.sort()
total=[]
for i in range(len(x)//2):
    total.append(x[i] + x[5-i])
print(max(total)-min(total))

