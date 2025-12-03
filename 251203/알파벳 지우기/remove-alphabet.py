a = input()
b = input()
x=''
y=''

for i in a:
    if i.isdigit() is False:
        continue
    else:
        x += i

for i in b:
    if i.isdigit() is False:
        continue
    else:
        y += i

print(int(x)+int(y))