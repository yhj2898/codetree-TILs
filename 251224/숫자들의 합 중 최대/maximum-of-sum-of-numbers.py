x, y = map(int, input().split())

max_sum = 0
for i in range(x,y+1):
    a = tuple(map(int, list(str(i))))
    total = sum(a)
    max_sum = max(max_sum,total)
print(max_sum)