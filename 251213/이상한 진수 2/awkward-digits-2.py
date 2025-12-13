a = list(input())

for i in range(len(a)):
    if a[i]=='0':
        a[i]='1'
        break
else:
    for j in range(len(a)-1,-1,-1):
        if a[j]=='1':
            a[j]='0'
            break

num=0
for i in range(len(a)):
    num = num*2 + int(a[i])
print(num)