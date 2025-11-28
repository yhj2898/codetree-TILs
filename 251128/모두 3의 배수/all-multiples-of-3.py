arr = [int(input()) for _ in range(5)]

x = True
for i in arr:
    if i %3 != 0:
        x = False

print(1 if x else 0)