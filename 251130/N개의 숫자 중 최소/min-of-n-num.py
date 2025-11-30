n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = 99999999999999

for i in a:
    if i < min_val:
        min_val = i
print(min_val, a.count(min_val))