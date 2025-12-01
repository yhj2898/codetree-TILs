n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_val = 0
for i in range(len(price)):
    for j in range(i,len(price)):
        m = price[j] - price[i]
        if m > max_val:
            max_val = m
print(max_val)