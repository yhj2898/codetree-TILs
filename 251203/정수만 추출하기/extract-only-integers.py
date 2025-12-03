a,b = input().split()
x=''
y=''
for i in a:
    if i.isdigit():
        x += i
    else:
        break

for i in b:
    if i.isdigit():
        y += i
    else:
        break

print(int(x)+int(y))