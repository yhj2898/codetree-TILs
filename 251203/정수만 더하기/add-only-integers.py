x = input()

total = 0

for i in x:
    if i.isdigit():
        total += int(i)
print(total)