a = list(input())
x1 = a[0]
x2 = a[1]
for i in range(len(a)):
    if a[i] == x2:
        a[i] = x1
print(''.join(a))