arr=[input() for _ in range(10)]
n=input()

cond=False
for s in arr:
    if s[-1]==n:
        print(s)
        cond=True

if cond is False:
    print('None')